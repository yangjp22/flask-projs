from flask import Flask
from settings import DevelopmentConfig
from exts import db
from .user.view import user_bp

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder="../static")
    app.config.from_object(DevelopmentConfig)
    app.register_blueprint(user_bp)
    db.init_app(app)
    

    return app