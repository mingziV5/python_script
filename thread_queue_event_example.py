#!/usr/bin/python
#coding:utf-8
from Queue import Queue
from threading import Thread,Event

def producer(out_q):
    while running:
        evt = Event()
        out_q.put = ((data,evt))
        #wait for the consumer to process the item
        evt.wait()

def consumer(in_q):
    while True:
        data,evt = in_q.get()
        #Indicat completion
        evt.set()
