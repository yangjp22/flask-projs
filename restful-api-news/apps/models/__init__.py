from exts import db
from datetime import datetime

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pub_datetime = db.Column(db.DateTime, default=datetime.now)