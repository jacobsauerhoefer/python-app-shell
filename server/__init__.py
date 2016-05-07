from flask import Flask, request, render_template, jsonify, Blueprint
from api import task_api
app = Flask(__name__, template_folder='../public')

@app.route('/')
def hello_world():
    return render_template('index.html')

app.register_blueprint(task_api)
