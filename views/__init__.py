# -*- coding: utf-8 -*-
# @Date    : 2017-07-30 21:46:32
# @Author  : lileilei
from tornado.web import RequestHandler
from  model.models import User
class BaseHander(RequestHandler):
    @property
    def db(self):
        return self.application.db
    def get_current_user(self):
        user_id = self.get_secure_cookie('user_id')
        if not user_id:
            return None
        return user_id

