#!/usr/bin/python
#coding:utf-8
#当消费者线程接受到结束信号后会将信号重新放回队列中，使得其他监听这个队列的消费者线程也能收到终止值
from Queue import Queue
from threading import Thread

#object that signals shutdown
_sentinel = object()

#A thread that producers data
def producer(out_q):
    while running:
        #Producer some data
        out_q.put(data)
    #put the sentinel on the queue to indicate completion
    out_q.put(_sentinel)

#A thread that consumer data
def consumer(in_q):
    while True:
        #get some data
        data = in_q.get()
        
        #check for sentinel
        if data is _sentine:
            in_q.put(_sentinel)
            break
        
        #Process the data
