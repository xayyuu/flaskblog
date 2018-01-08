# -*- coding: utf-8 -*-
from flask import Flask, render_template, url_for, redirect, request, flash, session, g, abort
from myapp import app
from model import article_tags, Category, Post, Tag, Comment, pageby, db
from werkzeug import secure_filename
from werkzeug.contrib.atom import AtomFeed
from flask_cache import Cache
from random import shuffle
from HTMLParser import HTMLParser
from re import sub
from sys import stderr
from traceback import print_exc
import os
import json
import time
from datetime import datetime
from form import CommentForm
from config import CATALOG

from . import auth


@auth.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
            flash(error)
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
            flash(error)
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('newpost'))
    return render_template('auth/login.html')