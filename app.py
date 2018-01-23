#!/usr/bin/env python
# encoding: utf-8


"""
@version: ??
@author: mum
@license: Apache Licence 
@contact: shuo502@163.com
@author: ‘yo‘
@site: http://github.com/shuo502
@software: PyCharm
@file: app.py.py
@time: 2018/1/23 15:29
"""
from flask import *
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
@app.rout('/in/')
#
def inx():
    pass
    return 'x'
if __name__ == '__main__':
    app.run(debug=True,port=8080)