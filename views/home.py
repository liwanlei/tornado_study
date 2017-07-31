# encoding: utf-8
"""
@author: lileilei
@site: 
@software: PyCharm
@file: home.py
@time: 2017/7/31 11:47
"""
from model.models import User,Tag,New,db_session
from views import  BaseHander
import re
from  libs.common import encrypt
def get_tag():
    return db_session.query(Tag).all()
class IndexHadnder(BaseHander):
    def get(self):
        tags=get_tag()
        titles=db_session.query(New).all()
        self.render('home.html',tags=tags,news=titles)
class LoginHadnder(BaseHander):
    def get(self):
        self.render('login.html',error_message=None)
    def post(self):
        error_message = {
            '100': '信息填写不完整',
            '101': '该用户不存在',
            '102': '密码错误',
        }
        email = self.get_argument('username', '')
        password = self.get_argument('password', '')
        if not(email and password):
            self.render('login.html',error_message=error_message['100'])
        user=User.get_by_username(email)
        if not  user:
            self.render('login.html', error_message=error_message['101'])
        if user.password!=encrypt(password):
            self.render('login.html', error_message=error_message['102'])
        self.set_secure_cookie("user_id", str(user.id), expires_days=7)
        self.redirect('/')
class RegHander(BaseHander):
    def get(self):
        self.render('reg.html',error_message='')
    def post(self):
        error_message={
            100:'用户已经存在',
            101:'邮箱已经注册!',
            102:'邮箱格式错误',
            103:'请确认两次输入密码是否一致',
            104:'请检查信息是否填写',
            105: '用户名在8-15个字符',
            115: '注册失败',
        }
        username = self.get_argument('username', '')
        password=self.get_argument('password','')
        password1=self.get_argument('password1','')
        email=self.get_argument('email','')
        if not (username and password and password1 and email):
            self.render('reg.html',error_message=error_message[104])
        if len(username)<8 or len(username)>15:
            self.render('reg.html', error_message=error_message[105])
        p3 = re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}|[^\._-][\w\.-]+@(?:[A-Za-z0-9]+\.)+[A-Za-z]+')
        emailor = p3.match(email)
        if not emailor:
            self.render('reg.html',error_message=error_message[102])
        user=User.get_by_username(username)
        if user:
            self.render('reg.html',error_message=error_message[100])
            return
        emasil=User.get_by_email(email)
        if emasil:
            self.render('reg.html',error_message=error_message[101])
            return
        try:
            User.new(username=username,email=email,password=password)
            self.redirect('/login')
            return
        except:
            self.render('reg.html', error_message=error_message[115])
            return
class LogoutHandler(BaseHander):
    def get(self):
        self.clear_cookie('user_id')
        self.redirect('/')
