# -*- coding: utf-8 -*-
# @Time    : 2017/7/29 21:03
# @Author  : lileilei
# @Site    : 
# @File    : databease.py
# @Software: PyCharm
from sqlalchemy import  create_engine
from  sqlalchemy.orm import  scoped_session,sessionmaker
from sqlalchemy.ext.declarative import  declarative_base
engine=create_engine('sqlite:///database.db',convert_unicode=True)
Base=declarative_base()
db_session=scoped_session(sessionmaker(bind=engine))
def create_all():
    Base.metadata.create_all(engine)
def drop_all():
    Base.metadata.drop_all(engine)
