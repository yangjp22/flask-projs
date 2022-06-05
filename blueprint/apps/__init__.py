from flask import Flask
from . import settings
from .user.views import userBp


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder="../static")
    app.config.from_object(settings)
    app.register_blueprint(userBp)

    print(app.config)
    return app