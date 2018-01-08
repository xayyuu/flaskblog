# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint)

from auth.views import *
from views import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
