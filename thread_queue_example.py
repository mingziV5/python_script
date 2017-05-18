#!/usr/bin/python
#coding:utf-8
#线程间交换数据，通信最安全做法是使用Queue，用put(),get()方法来操作队列
from Queue import Queue
from threading import Thread

def producer(out_q):
    while True:
        out_q.put(data)

def consumer(in_q):
    while True:
        data = in_q.get()

if __name__ == '__main__':
    q = Queue()
    t1 = Thread(target=consumer,args=(q,))
    t2 = Thread(target=producer,args=(q,))
    t1.start()
    t2.start()
