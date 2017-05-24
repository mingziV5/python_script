#!/usr/bin/python
#coding:utf-8
import socket
import os,sys,signal
"""
GET /index.html HTTP/1.1
Host: www.example.com
"""


#resp = "HTTP/1.1 200 OK\r\nContent-Length: 15\r\n\r\n<h1>hello world</h1>"
resp = "HTTP/1.1 200 OK\r\nContent-Length: "

listen_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
listen_fd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_fd.bind(('0.0.0.0',6666))
#backlog
listen_fd.listen(10)
#把sigchld信号交给init去回收
signal.signal(signal.SIGCHLD,signal.SIG_IGN)
while True:
    all_read = ''
    conn, addr = listen_fd.accept()
    pid = os.fork()
    if pid !=0:
        pass
    else:
        print conn, addr
        while "\r\n\r\n" not in all_read:
            read_data = conn.recv(1)
            all_read += read_data
        url_context = all_read.split(" ")[1]
        file_dir = '/home/ming/workspace/html' + url_context
#        if url_context == '/lagou.jpg'
        if os.path.isfile(file_dir):
            content_length = os.path.getsize(file_dir)
            file_context = ''
            with open(file_dir) as f:
                file_context = f.read()
            resp += str(content_length) + '\r\n\r\n' + file_context
        else:
            resp = "HTTP/1.1 404 NOT Found\r\nContent-Length: 12\r\n\r\n<h1>404</h1>"
        conn.send(resp)
        conn.close()
        sys.exit(0)
