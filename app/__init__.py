from app.views import api
from flask import Flask


def create_app(config='app.config.Config'):
    """Returns a Flask application."""
    app = Flask(__name__, static_folder=None)
    app.config.from_object(config)
    app.register_blueprint(api)
    return app
