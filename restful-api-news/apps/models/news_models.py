from exts import db
from datetime import datetime
from apps.models import BaseModel

class NewsType(BaseModel):
    __tablename__ = 'tbl_newstype'
    type_name = db.Column(db.String(64))


class News(BaseModel):
    __tablename__ = 'tbl_news'
    title = db.Column(db.String(64), nullable=False)
    content = db.Column(db.Text, nullable=False)

    news_type = db.Column(db.Integer, db.ForeignKey('tbl_newstype.id'))