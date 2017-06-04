#!/usr/bin/python
#coding:utf-8
import select
import socket

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM,0)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
listen_socket.bind(('0.0.0.0',8888))
listen_socket.listen(10)
epoll_socket = select.epoll()
epoll_socket.register(listen_socket.fileno(), select.EPOLLIN)

fd_socket = {
    listen_socket.fileno(): listen_socket,
}

#read 12345\r\n
#write 54321\r\n
while True:
    epoll_list = epoll_socket.poll()
    for fd, event in epoll_list:
        print fd,event
        if fd == listen_socket.fileno():
            conn,addr = listen_socket.accept()
            print conn,addr
            epoll_socket.register(conn.fileno(), select.EPOLLIN)
            fd_socket[conn.fileno()] = conn
        else:
            print fd_socket[fd].recv(1)
