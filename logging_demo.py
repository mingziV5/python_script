#!/usr/bin/python
#coding:utf-8
import logging,logging.handlers,logging.config
import os
import traceback
'''
通过函数，实例化一个logger对象(直接配置参数，或者通过配置文件加载参数即可)
函数实例化logger对象后，并将对象作为返回值，即return logger
其他模块直接调用模块中的函数即可调用

模块外调用
import logging_demo
def index():
    logging_demo.Writelog('api').info('just a test')

index()
'''
work_dir = os.path.dirname(os.path.realpath(__file__))
#定义写日志的函数，返回实例化的logger对象，直接配置logger参数的形式
def WriteLog(log_name):
    log_filename = '/tmp/test.log'
    log_level = logging.DEBUG
    log_format = logging.Formatter('%(asctime)s %(filename)s - [line:%(lineno)2d] - %(funcName)s %(levelname)s - %(name)s %(message)s')
    handler = logging.handlers.RotatingFileHandler(log_filename, mode='a', maxBytes=10*1024*1024, backupCount=5)
    handler.setFormatter(log_format)
    logger = logging.getLogger(log_name)
    logger.addHandler(handler)
    logger.setLevel(log_level)
    return logger

def WriteLogConf(log_name):
    log_conf =  os.path.join(work_dir, 'logging.conf')
    logging.config.fileConfig(log_conf)
    logger = logging.getLogger(log_name)
    return logger

if __name__ == '__main__':
    WriteLog('api').info('just a test')
    WriteLogConf('web').info('web test')
    WriteLogConf('api').info('api test')
    try:
        i = 1/0
    except:
        WriteLogConf('api').error('exception traceback %s' %traceback.format_exc())
