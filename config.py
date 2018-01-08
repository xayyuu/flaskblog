#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

"""
    config.py
    ~~~~~~~~~~~

    basic configuration

    :copyright: (c) 2013.
    :license: BSD, see LICENSE for more details.
"""
import os


DEBUG = True

# configuration page num
PER_PAGE = 10

# configuration mysql
#SQLALCHEMY_DATABASE_URI = "mysql://%s:%s@%s/%s" % ('root', 'root', '127.0.0.1', 'xyspurs')
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+ os.path.join(basedir, 'data.sqlite')

# proj code : zhuzi
SECRET_KEY =os.environ.get("SECRET_KEY_ZHUZI")
USERNAME = os.environ.get("USERNAME_ZHUZI")
PASSWORD = os.environ.get("PASSWORD_ZHUZI")


UPLOAD_FOLDER = './static/upload/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

RECAPTCHA_PUBLIC_KEY = '6Ld4rwITAAAAAKUD5AntlHi7HL36W2vHJQOIjQmA'
RECAPTCHA_PRIVATE_KEY = '6Ld4rwITAAAAAFE8nTS852QbsqCBx1mN8D4BqenE'

# 目錄
CATALOG = [u'Python', u'Algorithm', u'DevOps', u'AI', u"Life"]
