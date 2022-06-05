from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import or_, and_, not_
from .models import User
from exts import db
import hashlib

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['GET', 'POST'], endpoint='register')
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        pwd = request.form.get('pwd')
        repwd = request.form.get('repwd')
        phone = request.form.get('phone')

        if pwd == repwd:
            # 创建模型对象
            user = User()
            # 给对象属性赋值
            user.username = username
            user.pwd = hashlib.sha256(pwd.encode('utf-8')).hexdigest()
            user.phone = phone
            # 将有值的对象添加给session, 相当于一个容器
            db.session.add(user)
            # 提价数据
            db.session.commit()
            return redirect(url_for('user.login'))
        else:
            return 'pwd error'

    return render_template('user/register.html')


@user_bp.route('/show', endpoint='list')
def show():
    # 所有的实例
    # users = User.query.all()

    # filter_by
    # users = User.query.filter_by(username = 'fred')
    # user = User.query.filter_by(username = 'fred').first()

    # 主键查询
    # user = User.query.get(2)

    # filter查询
    # users = User.query.filter(User.username == 'fred').all()
    # user = User.query.filter(User.username == 'fred').first()
    # users = User.query.filter(User.age > 18).all()
    # users = User.query.filter(User.username.contains('fred')).all()
    # users = User.query.filter(User.username.like(r'%fred%')).all()
    # users = User.query.filter(or_(User.username.startswith('fred'), User.age > 18)).all()
    # users = User.query.filter(and_(User.username.startswith('fred'), User.age > 18)).all()
    # users = User.query.filter(not_(User.username.startswith('fred'))).all()

    # 排序 order_by
    users = User.query.order_by('username').all()
    # users = User.query.order_by(User.username).all()
    # users = User.query.order_by(-User.username).all()

    return render_template('user/show.html', users=users)


@user_bp.route('/login', methods=['POST', 'GET'], endpoint='login')
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        pwd = request.form.get('pwd')

        new_pwd = hashlib.sha256(pwd.encode('utf-8')).hexdigest()
        u_username = User.query.filter_by(username = username).first()
        print(u_username)
        if u_username.pwd == new_pwd:
            print('denglu chenggong')
            return redirect(url_for('user.list'))
        else:
            print('登录失败')
            return render_template('user/login.html', msg='Username or password is wrong')
    
    return render_template('user/login.html')


@user_bp.route('/delete', endpoint='delete')
def delete():
    idx = request.args.get('id')

    user = User.query.get(idx)
    
    return user