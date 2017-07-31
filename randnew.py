# -*- coding: utf-8 -*-
# @Time    : 2017/7/31 21:14
# @Author  : lileilei
# @File    : randnew.py
# @Software: PyCharm
import random
from model.models import  New
for i in range(1000):
    print(i)
    New.new(title1=(i),desc=(i*100),text=(i*10000),create_usid=random.randint(1,5),tag_id=random.randint(1,5))
