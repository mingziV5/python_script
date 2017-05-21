#!/usr/bin/python
#coding:utf-8

from threading import Thread
from Queue import Queue

class TestRing(Thread):
    def __init__(self,q_out,q_in,thread_name):
        Thread.__init__(self)
        self.q_out = q_out
        self.q_in = q_in
        self.thread_name = thread_name

    def run(self):
        while True:
            i = self.q_out.get()
            if i==10000:
                self.q_in.put(i)
                print '%s is done' %self.thread_name
                break
            i += 1
            print "put the i = %s,my name is %s" %(i,self.thread_name)
            self.q_in.put(i)

def main():
    q1 = Queue()
    q1.put(1)
    q2 = Queue()
    q3 = Queue()
    t1 = TestRing(q1,q2,'t1')
    t2 = TestRing(q2,q3,'t2')
    t3 = TestRing(q3,q1,'t3')
    
    t3.start()
    t2.start()
    t1.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == '__main__':
    main()
