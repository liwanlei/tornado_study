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
from  model.databease import db_session,engine,create_all
from  url import url_pattern
define('port',default=9000,help='run on the given port',type=int)
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
    tornado.ioloop.IOLoop.instance().start()