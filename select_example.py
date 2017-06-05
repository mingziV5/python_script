#/usr/bin/python
#coding:utf-8
import socket
import Queue
import select

message_queue = {}
input_list = []
output_list = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0',8888))
server.listen(5)
#设置为非阻塞
server.setblocking(False)
#将服务端加入监听列表
input_list.append(server)

while True:
    stdinput,stdoutput,stderr = select.select(input_list,output_list,input_list)
    #循环是否有客户端链接进来，当有客户端连接进来时候select将被触发
    for obj in stdinput:
        #判断当前触发的是不是服务端对象，当触发的对象是服务端对象时，说明有新的客户端连接进来了
        if obj == server:
            #接受客户端的连接，获取客户端对象和客户端地址信息
            conn, addr = server.accept()
            print conn,addr
            #将客户端对象也加入到监听的列表中，当客户端发送消息时select将触发
            input_list.append(conn)
            #为连接的客户端单独创建一个消息队列，用来保存客户端发送的消息
            message_queue[conn] = Queue.Queue()
        else:
            #由于客户端连接进来时服务端接收客户端连接请求，将客户端加入到了监听列表中（input_list），客户端发送信息时候会被触发
            #所以判断是否是客户端对象触发
            try:
                recv_data = obj.recv(1024)
                #客户端断开
                if recv_data:
                    print recv_data
                    recv_data = recv_data[::-1]
                    message_queue[obj].put(recv_data)
                    #将回复操作放到output列表中，让select监听
                    if obj not in output_list:
                        output_list.append(obj)
            except ConnectionResetError:
                #客户端断开连接，将客户端的监听从input列表中移除
                input_list.remove(obj)
                del message_queue[obj]
                print 'disconnected',obj
    
    #处理完input_list，对output_list处理，是否发送消息
    for sendobj in output_list:
        try:
            #如果消息队列中有消息，从消息队列中获取要发送的消息
            if not message_queue[sendobj].empty():
                #从该客户端对象的消息队列中获取要发送的消息
                send_data = message_queue[sendobj].get()
                sendobj.sendall(send_data)
            else:
                #将监听移除等待下一次客户端发送消息
                output_list.remove(sendobj)
        except ConnectionResetError:
            del message_queue[sendobj]
            output_list.remove(sendobj)
            print 'disconnected',senobj 
