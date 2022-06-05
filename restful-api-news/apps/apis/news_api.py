from exts import api
from flask_restful import Resource, fields, marshal_with
from flask import Blueprint
from apps.models.news_models import NewsType


news_bp = Blueprint('news_api', __name__, url_prefix='api')

news_type_fields = {
    'id': fields.Integer,
    'name': fields.String(attribute='type_name')
}

class NewsTypeResource(Resource):

    @marshal_with(news_type_fields)
    def get(self):
        types = NewsType.query.all()
        return types


api.add_resource(NewsTypeResource, '/newstype')