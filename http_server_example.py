#!/usr/bin/python
#coding:utf-8
import socket
import time

"""
GET /index.html HTTP/1.1
Host: www.example.com
"""


resp = "HTTP/1.1 200 OK\r\nContent-Length: 15\r\n\r\n<h1>hello world</h1>"

listen_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
listen_fd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_fd.bind(('0.0.0.0',6666))
listen_fd.listen(10)
while True:
    all_read = ''
    conn, addr = listen_fd.accept()
    print conn, addr
    while "\r\n\r\n" not in all_read:
        read_data = conn.recv(1)
        all_read += read_data
    print read_data
    conn.send(resp)
