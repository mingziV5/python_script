#!/usr/bin/python
#coding:utf-8
'''
1.accept
2.read
3.和上次read到的append
4.判断是否读到\r\n
5.如果没有读到继续等poll触发
6.如果读到了，处理反转逻辑，删除EPOLLIN，注册EPOLLOUT
7.删除EPOLLOUT，往外write,等write完了，close（）
'''
import select
import socket

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
listen_socket.setblocking(0)
listen_socket.bind(('0.0.0.0',8888))
listen_socket.listen(10)
epoll_socket = select.epoll()
epoll_socket.register(listen_socket.fileno(), select.EPOLLIN)

fd_socket = {
    listen_socket.fileno(): listen_socket,
}
requests = {}

#read 12345\r\n
#write 54321\r\n
while True:
    epoll_list = epoll_socket.poll()
    for fd, event in epoll_list:
        #print fd,event
        if fd == listen_socket.fileno():
            conn,addr = listen_socket.accept()
            print conn,addr
            conn.setblocking(0)
            epoll_socket.register(conn.fileno(), select.EPOLLIN)
            fd_socket[conn.fileno()] = conn
            requests[conn.fileno()] = ''
        elif event & select.EPOLLIN:
            requests[fd] += fd_socket[fd].recv(1)
            if '\r\n' in requests[fd]:
                requests[fd] = requests[fd][:-2][::-1] + requests[fd][-2::]
                print requests[fd]
                epoll_socket.modify(fd,select.EPOLLOUT)
        elif event & select.EPOLLOUT:
            bytes_writeen = fd_socket[fd].send(requests[fd])
            requests[fd] = requests[fd][bytes_writeen:]
            if len(requests[fd]) == 0:
                epoll_socket.modify(fd,select.EPOLLIN)
        elif event & select.EPOLLHUP:
            epoll_socket.unregister(fd)
            fd_socket[fd].close()
            fd_socket.pop(fd)
        elif event & select.EPOLLERR:
            epoll_socket.unregister(fd)
            fd_socket[fd].close()
            fd_socket.pop(fd)


