#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-29 21:20:33
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     : Login Form
# @Version : $Id$

from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import Required


class LoginForm(Form):
    name = StringField('Account', validators=[Required()])
    passwd = PasswordField('Passwd', validators=[Required()])
    remenber_me = BooleanField('keep me logged in')
    submit = SubmitField('sign in')


class RegFrom(object):
    name = StringField('Account', validators=[Required()])
    passwd = StringField('Passwd', validators=[Required()])
    submit = SubmitField('sign up')
