from flask import Flask
from blueprints.page import page


def create_app():
    """
    Create a Flask application using the app factory pattern.

    :return: Flask app
    """
    # By writing app = Flask(__name__), we name the flask instance as app.
    app = Flask(__name__, instance_relative_config=True)
    # Loading config module
    app.config.from_object('config.settings')
    # silent=True telling not to crush if setting.py does not exist
    app.config.from_pyfile('settings.py', silent=True)

    app.register_blueprint(page)


    return app
