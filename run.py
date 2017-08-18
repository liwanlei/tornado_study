# -*- coding: utf-8 -*-
# @Time    : 2017/7/30 20:35
# @Author  : lileilei
# @File    : run.py
# @Software: PyCharm
import  tornado.web
import tornado.httpserver
import  tornado.ioloop
import  tornado.options
from tornado.options import define,options
from  setting import setting
from  model.databease import db_session,engine,create_all
from  url import url_pattern
from pachong import *
define('port',default=5000,help='run on the given port',type=int)
class Application(tornado.web.Application):
    def __init__(self,handlers,**setting):
        tornado.web.Application.__init__(self,handlers,**setting)
        self.db=db_session
application=Application(url_pattern,**setting)
if __name__ =='__main__':
    # create_all()
    tornado.options.parse_command_line()
    http_server=tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.PeriodicCallback(Get_xinwen,3000*6).start()
    tornado.ioloop.PeriodicCallback(caijing,3000*6).start()
    tornado.ioloop.PeriodicCallback(lishi,3000*6).start()
    tornado.ioloop.PeriodicCallback(keyji,3000*6).start()
    tornado.ioloop.PeriodicCallback(junshi, 3000 * 6).start()
    tornado.ioloop.PeriodicCallback(shehui, 3000 * 6).start()
    tornado.ioloop.IOLoop.current().start()