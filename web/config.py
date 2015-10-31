#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-29 00:13:58
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = '123456'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


@staticmethod
def init_app(app):
    pass


class DevelopConfig(Config):
    DEBUG = True
    Mail_Server = ''
    mail_port = 555
    MAIL_USE_TLS = True
    MAIL_USERNAME = ''
    MAIL_PASSWD = ''
    SQLALCHEMY_DATABASE_URI = \
        'sqlite:///' + os.path.join(basedir, 'datdev.sqlite')


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')


class ProductionConfig(Config):
    """docstring for ProductionConfig"""
    SQLALCHEMY_DATABASE_URI = \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopConfig
}
