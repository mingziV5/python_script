#!/usr/bin/python
#coding:utf-8
import socket
import select

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('0.0.0.0',8888))
server.listen(5)
#因为socket默认是阻塞的，所以需要使用非阻塞模式.
server.setblocking(0)

#创建一个epoll对象
epoll = select.epoll()
#在服务端socket上面注册对读event的关注。一个读event随时会触发服务端socket去接受一个socket连接
epoll.register(server.fileno(),select.EPOLLIN)

try:
    #字典connections映射文件描述符到其对应的网络连接对象
    connections = {}
    requests = {}
    responses = {}
    while True:
        #查询epoll对象，看是否有任何关注的event被触发，参数是1表示，我们会等待1秒来看是否有event发生。
        #如果有任何我们感兴趣的event发生在这次查询之前，这个查询就会带着这些event的列表立即返回
        events = epoll.poll(1)
        #event作为一个序列的（fileno,event code）的元组返回，fileno是文件描述符的代名词，始终是一个整数
        for fileno,event in events:
            #如果是服务端产生event，表示有一个新的连接进来:
            if fileno == server.fileno():
                conn,addr = server.accept()
                print conn,addr
                #将新的socket设置成非阻塞
                conn.setblocking(0)
                #对新的socket注册成读（EPOLLIN）event的关注
                epoll.register(conn.fileno(),select.EPOLLIN)
                #将新的连接加入到字典中
                connections[conn.fileno()] = conn
                #初始化要接受的数据
                requests[conn.fileno()] = ''
            #如果发生一个读event，就读取从客户端发送过来的新数据
            elif event & select.EPOLLIN:
                print "recv data"
                #接受客户端发送过来的数据
                requests[fileno] += connections[fileno].recv(1024)
                #如果客户端退出，关闭客户端连接，取消所有的读和写的监听
                if not requests[fileno]:
                    connections[fileno].close()
                    #删除connections字典中的监听对象
                    del connecitons[fileno]
                    #删除接受数据字典中对应的句柄对象
                    #del requests[connections[fileno]]
                    print connections,requests
                    epoll.modify(fileno,0)
                else:
                    #一旦完成请求已收到，就注销对event的关注，注册对写（EPOLLOUT）event的关注，写event发生的时候，会回复数据给客户端
                    epoll.modify(fileno,select.EPOLLOUT)
                    #打印完成的请求，证明虽然与客户端的通信是交错进行的，但数据可以作为一个整体来组装和处理
                    print requests[fileno]
            elif event & select.EPOLLOUT:
                print "send data"
                bytes_writeen = connections[fileno].send(requests[fileno])
                requests[fileno] = requests[fileno][bytes_writeen:]
                if len(requests[fileno]) == 0:
                    #一旦完成的响应数据发送完成，就不再关注写event
                    epoll.modify(fileno,select.EPOLLIN)
            
             

            #HUP(挂起) event表明客户端socket已经断开，所以服务端也需要关闭。
            #没有必要注册对HUP event的关注 。在socket上面，他们总是会被epoll对象注册
            elif event & select.EPOLLHUP:
                print 'end hup'
                #注销对此socket连接的关注
                epoll.unregister(fileno)
                #关闭socket连接
                connections[fileno].close()
                del connecitons[fileno]
finally:
    #打开的socket连接不需要关闭，因为python会在程序结束的时候关闭，这里显示关闭
    epoll.unregister(server.fileno())
    epoll.close()
    server.close()
