#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-30 19:33:06
# @Author  : zhuguangzu (guangzu_zhu@163.com)
# @Link    : http://blog.zhuguangzu.xyz
# DESC     :
# @Version : $Id$

from flask import Blueprint
from . import views, errors

main = Blueprint('main', __name__)

