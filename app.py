#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging
import os
from flask import *
app = Flask(__name__)
if 'PORT' in os.environ:
    port = int(os.environ['PORT'])
else:
    port = 8080

@app.errorhandler(404)
def page_not_found(e):
    return str(404)

@app.route("/")
def index():
    return "hello"

if __name__ == '__main__':

    try:
        app.run(host='0.0.0.0', port=port,debug=True)
        from wsgiref.simple_server import make_server
        httpd = make_server('0.0.0.0', port, app)
        httpd.serve_forever()
    except Exception as e:
        logging.exception(e, stack_info=True)
