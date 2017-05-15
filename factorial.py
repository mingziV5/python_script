#!/usr/bin/python
#coding:utf-8
import multiprocessing

def factorial(num):
    ret =1
    for i in range(1,num+1):
        ret *= i
    return ret

if __name__ == '__main__':
    l = range(1,1000)
    #l_map = map(factorial,l)
    #l_reduce = reduce(lambda x,y:x*y , l_map)
    #print l_reduce

    pool_size=multiprocessing.cpu_count()*2
    pool=multiprocessing.Pool(processes=pool_size)

    l_outputs = pool.map(factorial,l)

    pool.close()
    pool.join()

    #print l_outputs
    #print  reduce(lambda x,y:x*y , l_outputs)
