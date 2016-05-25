""" Server """

from app import APP, render_template
import app.api as api
# APP = Flask(__name__, template_folder='../../public')

@APP.route('/')
def hello_world():
    """ Function Comment """
    return render_template('index.html')

APP.register_blueprint(api.task_api)

if __name__ == '__main__':
    APP.run(debug=True)