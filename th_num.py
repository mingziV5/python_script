#!/usr/bin/python
#coding:utf-8
import threading
import time

count_num = 0 
def count_plus():
    global count_num
    for i in range(10000):
        count_num += 1

thread_list = []
for i in range(10):
    t = threading.Thread(target=count_plus)
    t.start()

while True:
    if threading.activeCount() != 1:
        pass
    else:
        print count_num
        break
