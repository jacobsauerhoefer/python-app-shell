#!/usr/bin/env python
""" Module Comment """

from flask import Flask, render_template
from api.task_api import task_api
APP = Flask(__name__, template_folder='../../public')

@APP.route('/')
def hello_world():
    """ Function Comment """
    return render_template('index.html')

APP.register_blueprint(task_api)

if __name__ == '__main__':
    APP.run(debug=True)
