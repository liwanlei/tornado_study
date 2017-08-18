# encoding: utf-8
"""
@author: lileilei
@site: 
@software: PyCharm
@file: home.py
@time: 2017/7/31 11:47
"""
from model.models import User,Tag,New,db_session,Comment
from views import  BaseHander
import tornado.web
import re
from  libs.common import encrypt
from libs.fenye import  Pagination
def get_tag():
    return db_session.query(Tag).all()
class IndexHadnder(BaseHander):
    def get(self,page=1):
        tags=get_tag()
        count=New.get_count()
        obj=Pagination(page,count)
        titles = db_session.query(New).order_by(New.create_time.desc())[int(obj.start):(int(page)) * (12)]
        str_page = obj.string_pager('/index/')
        self.render('home.html', tags=tags, news=titles, str_page=str_page)
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
        self.redirect('/index/1')
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
        self.redirect('/index/1')
class TagHadnder(BaseHander):
    def get(self,id=1,page=1):
        tags=get_tag()
        count=db_session.query(New).filter(New.tag_id==1).all()
        obj=Pagination(page,len(count))
        titles=db_session.query(New).order_by(New.create_time.desc()).filter_by(tag_id=id).all()[obj.start:int(page)*(12)]
        str_page = obj.string_pager('/tag/%s/'%id)
        self.render('tag.html',tags=tags,news=titles,str_page=str_page,id=id)
tags=''
titles=''
comments=''
class NewoneHadnder(BaseHander):
    def get(self,id):
        global  tags,titles,comments
        tags=get_tag()
        titles=db_session.query(New).filter_by(id=id).first()
        comment=db_session.query(Comment).filter_by(post_id=id).all()
        if len(comment)<=0:
            comments=''
        else:
            comments=comment
        self.render('one.html',tags=tags,news=titles,comments=comments,err_message='')
    @tornado.web.authenticated
    def post(self,id, *args, **kwargs):
        user = self.current_user
        comment = self.get_argument('comment', '')
        if not (user and comment):
            self.render('one.html', tags=tags, news=titles, comments=comments,err_message='评论内容不能为空')
            return
        try:
            Comment.new(post_id=id,user_id=user.id,comment=comment)
            self.redirect('/one/%s'%id)
            return
        except:
            self.render('one.html', tags=tags, news=titles, comments=comments,err_message='评论失败')
            return