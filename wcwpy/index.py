#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os,sys
import re
sys.path.insert(0, '/Users/wangchenwei/Documents/python/pyframwork/wcwpy/http') # or sys.path.append('/path/to/application/app/folder')
sys.path.insert(0, '/Users/wangchenwei/Documents/python/pyframwork/controller')
import httpc
import imp
# from indexController import *

#global WEBPATH = "/Users/wangchenwei/Documents/python/pyframwork/wcwpy/"

def entrance(evn) :
    
    ap = httpc.http(evn)
    print(ap.getMethod())
    module = __import__('indexController')
    controller = getattr(module,ap.getController()) ##获取对象
    mtd = getattr(controller(),ap.getMethod())   ##获取方法
    resp = mtd() ##执行方法
    # index = indexController()
    print(resp)
    return  resp
