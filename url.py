# encoding: utf-8
"""
@author: lileilei
@site: 
@software: PyCharm
@file: url.py
@time: 2017/7/31 12:25
"""
from views.home import IndexHadnder,LoginHadnder,RegHander,LogoutHandler
url_pattern=[
    ('/',IndexHadnder),
    ('/login',LoginHadnder),
    ('/reg',RegHander),
    ('/log',LogoutHandler)
]