# -*- coding: utf-8 -*-
# @Time    : 2017/7/30 20:33
# @Author  : lileilei
# @Site    : 
# @File    : setting.py
# @Software: PyCharm
from os import path
DEBUG=True
setting={
    'debug': DEBUG,
    'xsrf_cookies': True,
    'static_path': path.join(path.dirname(__file__), 'static'),
    'template_path': path.join(path.dirname(__file__), 'templates'),
}