from flask import Flask
from settings import DevelopmentConfig
from flask_script import Manager
from database import db
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)

class Role(db.Model):
    __tablename__ = 'tbl_role'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    users = db.relationship("User", backref='role')


class User(db.Model):
    __tablename__ = 'tbl_user'
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(128), unique=True)
    phone = db.Column(db.String(128), unique=True)
    pwd = db.Column(db.String(128))
    id = db.Column(db.Integer, primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('tbl_role.id'))






@app.route('/index')
def hello():
    return 'hello index'

if __name__ == '__main__':
    manager = Manager(app)

    Migrate(app, db)
    manager.add_command('db', MigrateCommand)
    
    manager.run()