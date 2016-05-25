from flask import Flask, render_template
import api as api

APP = Flask(__name__, template_folder='./public', instance_relative_config=True)

@APP.route('/')
def hello_world():
    """ Function Comment """
    return render_template('index.html')

APP.register_blueprint(api.task_api)
