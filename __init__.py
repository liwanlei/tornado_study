# encoding: utf-8
'''
@author: lileilei
@file: __init__.py
@time: 2017/5/6 10:33
'''
from flask import Flask
from flask_bootstrap import Bootstrap
from  flask_sqlalchemy import SQLAlchemy
from  flask_mail import Mail
from conf import loadconfig
import os
os.environ['MODE'] = 'dev'
app=Flask(__name__)
config = loadconfig.lod_config()
app.config.from_object(config)
db=SQLAlchemy(app)
bootstrp=Bootstrap(app)
mail=Mail(app)
from  app import views,models