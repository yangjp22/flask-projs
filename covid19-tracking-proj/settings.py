class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:604030@127.0.0.1:3306/covid'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

class DevelopmentConfig(Config):
    ENV = 'development'

class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://yftnitapytnniy:2ffa5338514737e3f4b2170994297a49fae6a4d170eea1e200a5191525995bed@ec2-52-200-111-186.compute-1.amazonaws.com:5432/daa3f3avjbqo41'