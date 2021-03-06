#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-29 00:08:22
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     : init scrpt
# @Version : $Id$

from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.email import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from config import config
from .main import main as main_blueprint

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    db.init_app(app)
    app.register_blueprint(main_blueprint)

    return app
