# -*- coding: utf-8 -*-
# @Time    : 2017/7/30 20:35
# @Author  : lileilei
# @Site    : 
# @File    : run.py
# @Software: PyCharm
import  tornado.web
import tornado.httpserver
import  tornado.ioloop
import  tornado.options
from tornado.options import define,options
from  setting import setting
from  mod.databease import db_session,engine
define('port',default=8000,help='run on the given port',type=int)
class Application(tornado.web.Application):
    def __init__(self,**setting):
        tornado.web.Application.__init__(self,**setting)
        self.db=db_session
application=Application(**setting)
if __name__ =='__main__':
    tornado.options.parse_command_line()
    http_server=tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()