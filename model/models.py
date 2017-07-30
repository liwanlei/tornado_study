# -*- coding: utf-8 -*-
# @Time    : 2017/7/29 22:11
# @Author  : lileilei
# @Site    : 
# @File    : models.py
# @Software: PyCharm
from model.databease import Base,db_session
from  libs.common import encry
import  datetime
from  model.databease import create_all
from sqlalchemy import  Column,Integer,DateTime,Boolean,String,ForeignKey,desc,asc
from sqlalchemy.orm import  relationship,backref
class Admin(Base):
    __tablename__='admins'
    id=Column(Integer(),primary_key=True)
    username=Column(String(64))
    email=Column(String(32))
    password=Column(String(64))
    last_log_ip=Column(String(16))
    update_time=Column(DateTime())
    status=Column(Integer())
    def __init__(self,id,username,email,realname):
        self.id=id
        self.username=username
        self.email=email
        self.realname=realname
    def __repr__(self):
        return self.username
    def new(self,username,password,realnem,email):
        '''add new user '''
        new=Admin(username=username,email=email,realname=realnem)
        new.password=encry(password)
        new.status=1
        new.update_time=datetime.datetime.now()
        new.last_log_ip=''
        db_session.add(new)
        try:
            db_session.commit()
        except:
            db_session.rollback()
    def update_password(self,password):
        new_password=encry(password)
        updatemi=datetime.datetime.now()
        update = {
            Admin.password: password,
            Admin.update_time: updatemi
        }
        db_session.query(Admin).filter(Admin.id == self.id).update(update)
        try:
            db_session.commit()
        except:
            db_session.rollback()
    @classmethod
    def get_count(cls):
        return  db_session.query(Admin).count()
    @classmethod
    def initialize(cls,item):
        if not item:
            return  None
        id=item.id
        username=item.username
        email=item.email
        realname=item.realname
        if not id:
            return  None
        return  cls(id,username,email,realname)
    @classmethod
    def get_by_username(cls,username):
        item=db_session.filter(username=username).first()
        return  item and cls.initialize(item)
    @classmethod
    def get_by_email(cls, email):
        item = db_session.filter(email=email).first()
        return item and cls.initialize(item)
    @classmethod
    def get_by_id(cls, id):
        item = db_session.filter(id=id).first()
        return item and cls.initialize(item)


if __name__=='__main__':
    create_all()