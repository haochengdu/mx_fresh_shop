#!/usr/bin/python3.5.2
# -*- coding: utf-8 -*-
"""
@Time    : 2018/12/28 14:09
@Author  : TX
@File    : test.py
@Software: PyCharm
"""
# 获取当前文件的路径（运行脚本）
import os

import sys

print(os.path.realpath(__file__))
print(os.getcwd())
pwd = os.path.dirname(os.path.realpath(__file__))
# 获取项目的跟目录
sys.path.append(pwd + "../")

print(os.getcwd())
for i in range(10):
    print(i)

