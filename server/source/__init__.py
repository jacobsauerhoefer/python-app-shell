""" Initialize App Directory """

from flask import Flask, render_template

APP = Flask(__name__, template_folder='../../public', instance_relative_config=True)
