#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-27 21:42:41
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

from __init__ import *

app = flask.Flask(__name__)

manager = flask.ext.script.Manager(app)
bootstrap = flask.ext.bootstrap.Bootstrap(app)
render_template = flask.render_template
host = config.ipaddr
port = config.port


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def users(name):
    return render_template('users.html', name=name)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def intrate_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(host=host, port=port)
