#!/usr/bin/python
#coding:utf-8
import time

class Th():
    def __init__(self,thread_name):
        self.thread_name = thread_name

    def run(self):
        print 'This is thread ' + self.thread_name
        for i in range(5):
            time.sleep(1)
            print str(i)
        print self.thread_name + ' is over'

if __name__ == '__main__':
    th = Th('T1')
    from threading import Thread
    t = Thread(target=th.run)
    t.start()
    print 'Main over \n'
