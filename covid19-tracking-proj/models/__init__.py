from exts import db
from datetime import datetime


class Details(db.Model):
    __tablename__ = 'tbl_details'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    update_time = db.Column(db.DateTime, default=datetime.now)
    state = db.Column(db.String(16), nullable=True)
    confirm = db.Column(db.Integer)
    confirm_add = db.Column(db.Integer)
    heal = db.Column(db.Integer)
    dead = db.Column(db.Integer)


class History(db.Model):
    __tablename__ = 'tbl_history'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ds = db.Column(db.DateTime, default=datetime.now)
    confirm = db.Column(db.Integer)
    confirm_add = db.Column(db.Integer)
    suspect = db.Column(db.Integer)
    suspect_add = db.Column(db.Integer)
    heal = db.Column(db.Integer)
    dead = db.Column(db.Integer)
    dead_add = db.Column(db.Integer)


class HotSearch(db.Model):
    __tablename__ = 'tbl_hotsearch'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dt = db.Column(db.DateTime, default=datetime.now)
    content = db.Column(db.String(256))

