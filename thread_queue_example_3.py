#!/usr/bin/python
#coding:utf-8
from threading import Thread
from Queue import Queue
import random,time

#producer
class Producer(Thread):
    def __init__(self,q,thread_name):
        Thread.__init__(self)
        self.setName(thread_name)
        self.q = q

    def run(self):
        for i in range(10):
            randomnum=random.randint(1,999)
            self.q.put(randomnum)
            print "%s: %s is producing %d to the queue!" % (time.ctime(), self.getName(), randomnum)
            time.sleep(1)
        print "%s: %s finished!" %(time.ctime(), self.getName())

class Consumer_even(Thread):
    def __init__(self,q,thread_name):
        Thread.__init__(self)
        self.setName(thread_name)
        self.q = q

    def run(self):
        while True:
            try:
                get_num = self.q.get(1,5)
                if get_num%2 == 0:
                    print "%s: %s is consuming. %d in the queue is consumed!" % (time.ctime(),self.getName(),get_num)
                    time.sleep(2)
                else:
                    self.q.put(get_num)
                    time.sleep(2)
            except:
                print "%s: %s finished!" %(time.ctime(),self.getName())
                break

class Consumer_odd(Thread):
    def __init__(self,q,thread_name):
        Thread.__init__(self)
        self.setName(thread_name)
        self.q = q

    def run(self):
        while True:
            try:
                get_num = self.q.get(1,5)
                if get_num%2 == 1:
                    print "%s: %s is consuming. %d in the queue is consumed!" % (time.ctime(), self.getName(), get_num)
                    time.sleep(2)
                else:
                    self.q.put(get_num)
                    time.sleep(2)
            except:
                print "%s: %s finished!" % (time.ctime(), self.getName())
                break

def main():
    queue = Queue()
    pro = Producer(queue,'producer')
    con_even = Consumer_even(queue,'con_even')
    con_odd = Consumer_odd(queue,'con_odd')
    
    pro.start()
    con_even.start()
    con_odd.start()

    pro.join()
    con_even.join()
    con_odd.join()

    print 'All threads terminate!'

if __name__ == '__main__':
    main()



        
