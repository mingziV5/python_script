#!/usr/bin/python
#coding:utf-8
import ConfigParser

def getConfig(filename,section=''):
    cf = ConfigParser.ConfigParser()
    cf.read(filename)
    cf_items = dict(cf.items(section)) if cf.has_section(section) else {}
    return cf_items

if __name__ == '__main__':
    conf = getConfig('config_parser.conf','web')
    print conf
