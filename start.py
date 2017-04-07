#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server
import os
from wcwpy.index import *

Port = 9098
IP = '127.0.0.1'
def application(environ, start_response):
    r = entrance(environ)
    f = open('wcwpy/pid', 'w')
    pid = os.getpid()
    f.write(str(pid))
    f.close()
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [r.encode('utf-8')]


# 创建一个服务器
httpd = make_server(IP, Port, application)
print('Serving HTTP on port '+str(Port)+'...')
# 开始监听HTTP请求:
httpd.serve_forever()