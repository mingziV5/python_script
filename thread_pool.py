#!/usr/bin/python
#coding:utf-8

from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor

def test_function(num1,num2):
    print num1 + num2
    return num1 + num2

future = executor.submit(test_funciton,1,2)
print future.result()
