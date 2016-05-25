from application import app, render_template
import api as api

@app.route('/')
def hello_world():
    """ Function Comment """
    return render_template('index.html')

app.register_blueprint(api.task_api)
