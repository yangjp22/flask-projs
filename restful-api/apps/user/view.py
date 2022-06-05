from flask import Blueprint,  request
from .models import User, Friend
from exts import db, api
from flask_restful import Resource, fields, marshal_with, reqparse, marshal

user_bp = Blueprint('user', __name__, url_prefix="/api")


class DeleteItem(fields.Raw):
    def format(self, value):
        return '删除' if value else '未删除'

user_field_1 = {
    'id': fields.Integer(attribute='id'),
    'uri': fields.Url('userDetail', absolute=True),
    'rdatetime': fields.DateTime,
}

user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'pwd': fields.String,
    'phone': fields.String,
    'rdatetime': fields.DateTime,
    'Delete': DeleteItem(attribute='isDelete')
}

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True, help='Username')
parser.add_argument('pwd', type=str, required=True, help='password')
parser.add_argument('phone', type=str, required=True, help='phone')
parser.add_argument('isDelete', type=bool, required=True, help='is deleted?')
# parser.add_argument('icon', type=FileStorage, location=['files'])



class UserResource(Resource):
    
    @marshal_with(user_field_1)
    def get(self):
        users = User.query.all()
        return users

    def post(self):
        args = parser.parse_args()
        username = args.get('username')
        pwd = args.get('pwd')
        phone = args.get('phone')
        isDelete = args.get('isDelete')

        user = User(username=username, pwd=pwd, phone=phone, isDelete=isDelete)

        db.session.add(user)
        db.session.commit()

        return {'msg': 'add successfully...'}

    def put(self):
        return {'msg': 'put'}

    def delete(self):
        return {'msg': 'delete'}


class UserSingleResource(Resource):
    @marshal_with(user_fields)
    def get(self, id):
        user = User.query.get(id)
        return user


class UserFriendResource(Resource):

    def get(self, id):
        friends = Friend.query.filter(Friend.uid == id).all()
        user = User.query.get(id)

        friendList = [User.query.get(friend.fid) for friend in friends]

        data = {
            'username': user.username,
            'number': len(friendList),
            'friends': marshal(friendList, user_fields)
        }

        return data

    
    def delete(self, id, fid):
        pass



api.add_resource(UserResource, '/user', endpoint='users')
api.add_resource(UserSingleResource, '/user/<int:id>', endpoint='userDetail')
api.add_resource(UserFriendResource, '/friend/<int:id>', endpoint='freind')