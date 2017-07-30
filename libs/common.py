# -*- coding: utf-8 -*-
# @Time    : 2017/7/29 22:15
# @Author  : lileilei
# @Site    : 
# @File    : common.py
# @Software: PyCharm
import hashlib
from datetime import  datetime
import  json
def encry(key):
    hash1=hashlib.md5()
    hash1.update(key)
    return  hash1.hexdigest()
