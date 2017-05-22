#!/usr/bin/python
#coding:utf-8

from threading import Thread
from Queue import Queue

class TestRing(Thread):
    def __init__(self,q,thread_num,thread_name):
        Thread.__init__(self)
        #self.q_out = q_out
        #self.q_in = q_in
        self.q = q
        self.thread_num = thread_num
        self.thread_name = thread_name

    def run(self):
        while True:
            i,q_num = self.q.get()
            if i==10000:
                self.q.put((i,q_num))
                print '%s is done' %self.thread_name
                break
            elif q_num%10 == self.thread_num and i != 10000:
                i += 1
                q_num += 1
                print "put the i = %s,my name is %s" %(i,self.thread_name)
                self.q.put((i,q_num))
            else:
                self.q.put((i,q_num))

def main():
    q1 = Queue()
    q1.put((1,1))
    thread_list = []
    for i in range(10):
        t1 = TestRing(q1,i,str(i))
        thread_list.append(t1)
        t1.start()
    for t in thread_list:
        t.join  

if __name__ == '__main__':
    main()
