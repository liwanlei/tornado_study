# encoding: utf-8
"""
@author: lileilei
@site: 
@software: PyCharm
@file: url.py
@time: 2017/7/31 12:25
"""
from views.home import IndexHadnder,LoginHadnder,RegHander,LogoutHandler,TagHadnder,NewoneHadnder
url_pattern=[
    ('/index/(?P<page>\d*)',IndexHadnder),
    ('/login',LoginHadnder),
    ('/reg',RegHander),
    ('/log',LogoutHandler),
    ('/tag/(?P<id>\d*)/(?P<page>\d*)',TagHadnder),
    ('/one/(?P<id>\d*)',NewoneHadnder)
]