# -*- coding: utf-8 -*-
# @Time    : 2017/7/29 22:11
# @Author  : lileilei
# @Site    : 
# @File    : models.py
# @Software: PyCharm
from model.databease import Base,db_session
from  libs.common import encrypt
import  datetime
from  model.databease import create_all
from sqlalchemy import  Column,Integer,DateTime,Boolean,String,ForeignKey,desc,asc,Text
from sqlalchemy.orm import  relationship,backref
class User(Base):
    __tablename__='users'
    id=Column(Integer(),primary_key=True)
    username=Column(String(64),unique=True,index=True)
    email=Column(String(32),unique=True,index=True)
    password=Column(String(64))
    last_log_ip=Column(String(16))
    update_time=Column(DateTime())
    status=Column(Integer())
    news=relationship('New',backref='users',)
    def __init__(self,username,email):
        self.username=username
        self.email=email
    def __repr__(self):
        return self.username
    @classmethod
    def new(cls,username,password,email):
        '''add new user '''
        new=User(username=username,email=email)
        new.password=encrypt(password)
        new.status=1
        new.update_time=datetime.datetime.now()
        new.last_log_ip=''
        db_session.add(new)
        try:
            db_session.commit()
        except:
            db_session.rollback()
    def update_password(self,password):
        new_password=encrypt(password)
        updatemi=datetime.datetime.now()
        update = {
            User.password: password,
            User.update_time: updatemi
        }
        db_session.query(User).filter(User.id == self.id).update(update)
        try:
            db_session.commit()
        except:
            db_session.rollback()
    @classmethod
    def get_count(cls):
        return  db_session.query(User).count()
    @classmethod
    def get_by_username(cls,username):
        item=db_session.query(User).filter_by(username=username).first()
        return  item
    @classmethod
    def get_by_email(cls, email):
        item = db_session.query(User).filter(User.email==email).first()
        return item
    @classmethod
    def get_by_id(cls, id):
        item = db_session.query(User).filter(User.id==id).first()
        return item
class New(Base):
    __tablename__='news'
    id=Column(Integer(),primary_key=True)
    title=Column(String(252),index=True)
    desc=Column(String(64),index=True)
    text=Column(Text)
    create_time=Column(DateTime(),default=datetime.datetime.now())
    create_usid=Column(Integer(),ForeignKey('users.id'))
    tag_id=Column(Integer(),ForeignKey('tags.id'))
    def __repr__(self):
        return self.title
    @classmethod
    def get_count(cls):
        return  db_session.query(New).count()
    @classmethod
    def new(cls,title1,desc,text,create_usid,tag_id):
        '''add new user '''
        new=New(title=title1,desc=desc,text=text,create_usid=create_usid,tag_id=tag_id)
        new.create_time=datetime.datetime.now()
        db_session.add(new)
        try:
            db_session.commit()
        except:
            db_session.rollback()
    @classmethod
    def get_by_id(cls, id):
        item = db_session.query(New).filter(New.id==id).first()
        return item
    @classmethod
    def get_by_title(cls, title):
        item = db_session.query(New).filter(New.title==title).first()
        return item
    @classmethod
    def get_by_tag_id(cls, tag_id):
        item = db_session.query(New).filter(New.tag_id == tag_id).all()
        return item
class Tag(Base):
    __tablename__='tags'
    id=Column(Integer(),primary_key=True)
    tag=Column(String(64),unique=True,index=True)
    news = relationship('New', backref='tags', )
    def __repr__(self):
        return self.tag
    @classmethod
    def get_count(cls):
        return  db_session.query(Tag).count()
    def new(self,tag):
        '''add new tag '''
        new=Tag(tag=tag)
        db_session.add(new)
        try:
            db_session.commit()
        except:
            db_session.rollback()
    @classmethod
    def get_by_id(cls, id):
        item = db_session.query(Tag).filter(Tag.id==id).first()
        return item
    @classmethod
    def get_by_tag(cls, tag):
        item = db_session.query(Tag).filter(Tag.tag==tag).first()
        return item
