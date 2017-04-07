#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from urllib import parse

class http :

    host = ''
    method = ''
    path = ''
    res_length = 0
    POST = ''
    GET = ''
    resquet = {}
    def __init__(self, evn) :
        http.host = evn.get('HTTP_HOST')
        http.method = evn['REQUEST_METHOD']
        http.path = evn.get('PATH_INFO')
        http.res_length = evn.get('CONTENT_LENGTH')
        s = evn.get('wsgi.input').read(int(http.res_length))
        http.POST= parse.parse_qs(s.decode('utf-8'))
        http.GET = parse.parse_qs(evn['QUERY_STRING']) 
        # http.resquet = {'Host': host, 'Method': method, 'Path': path}
    ##解析http请求
    def resolve() :
        return {'Host': host, 'Method': method, 'Path': path}

    def getHost(self):
        return http.path

    def _POST(self,name,index = 0):
        return http.POST[name][index]
    
    def _GET(self,name,index = 0):
        return http.GET[name][index]

    def getController(self):
        controller = '' ##控制器
        res = http.path.split('/')
        controller = res[1]
        if controller == '':
            controller = 'index'+'Controller'
        else:
            controller = controller+'Controller'
        return controller
    
    def getMethod(self):
        Method = '' ##方法
        res = http.path.split('/')
        Method = res[2]
        if Method == '':
            Method = 'index'
        return Method