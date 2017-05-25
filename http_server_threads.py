#!/usr/bin/python
#coding:utf-8
import socket
import os,sys,signal
from threading import Thread
from Queue import Queue
"""
GET /index.html HTTP/1.1
Host: www.example.com
"""
def producer():
    while True:
        conn,addr = listen_fd.accept()
        q.put(conn)

def worker():
    resp = "HTTP/1.1 200 OK\r\nContent-Length: "
    while True:
        conn = q.get()
        all_read = ''
        while "\r\n\r\n" not in all_read:
            read_data = conn.recv(1)
            all_read += read_data
        url_context = all_read.split(" ")[1]
        file_dir = '../html' + url_context
        print file_dir
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


listen_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
listen_fd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_fd.bind(('0.0.0.0',6666))
listen_fd.listen(10)

q = Queue()

for j in range(10):
    t = Thread(target=worker)
    t.daemon = True
    t.start()

for i in range(2):
    t = Thread(target=producer)
    t.daemon = True
    t.start()
    t.join()
