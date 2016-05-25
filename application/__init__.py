from flask import Flask, render_template
app = Flask(__name__, template_folder='./public', instance_relative_config=True)

import application.views
