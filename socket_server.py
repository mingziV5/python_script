#!/usr/bin/python
#coding:utf-8
import socket

HOST = ''
PORT = 9999
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(2)
conn,addr = s.accept()

print 'Got connetciton from: ', addr

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)
conn.close()
