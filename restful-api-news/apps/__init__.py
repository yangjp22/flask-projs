from flask import Flask
from settings import DevelopmentConfig
from exts import db, api, cors
from apps.apis.news_api import news_bp

def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder="../static")
    app.config.from_object(DevelopmentConfig)

    app.register_blueprint(news_bp)

    cors.init_app(app, support_credentials=True)
    db.init_app(app)
    api.init_app(app)

    return app