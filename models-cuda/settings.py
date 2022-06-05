class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:604030@127.0.0.1:3306/flask01'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = True

class DevelopmentConfig(Config):
    ENV = 'development'

class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = True