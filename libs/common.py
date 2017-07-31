# -*- coding: utf-8 -*-
# @Time    : 2017/7/29 22:15
# @Author  : lileilei
# @Site    : 
# @File    : common.py
# @Software: PyCharm
import hashlib
from datetime import  datetime
import  json
def encrypt(key):
    hash = hashlib.md5()
    hash.update(key.encode("utf-8"))
    return hash.hexdigest()