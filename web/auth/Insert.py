#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-30 16:52:29
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

from dbs import Role, User
import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

admin_role = Role(name='Admin')
mod_role = Role(name='Moderator')
user_role = Role(name='User')
user_john = User(username='user_john', role=admin_role)
user_susan = User(username='user_susan', role=user_role)
user_david = User(username='user_david', role=user_role)


db.session.add_all([admin_role, mod_role, user_role,user_john, user_susan, user_david])
db.session.commit()