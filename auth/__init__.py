#coding=utf-8


# for auth
from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views