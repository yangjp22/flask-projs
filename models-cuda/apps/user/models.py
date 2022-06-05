from exts import db
from datetime import datetime

class User(db.Model):
    __tablename__ = 'tbl_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), nullable=False)
    pwd = db.Column(db.String(64), nullable=False)
    phone = db.Column(db.String(11), nullable=False, unique=True)
    rdatetime = db.Column(db.DateTime, default=datetime.now)
    isDelete = db.Column(db.Boolean, default=0)

    def __str__(self):
        return self.username