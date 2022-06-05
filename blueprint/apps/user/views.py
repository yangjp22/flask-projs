from flask import Blueprint, render_template, request, redirect, url_for
from .models import User


userBp = Blueprint('user', __name__)
userList = []

@userBp.route('/')
def userCenter():

    return render_template('user/show.html', users=userList)

@userBp.route('/register', methods=['POST', 'GET'], endpoint="register")
def userRegister():
    if request.method == 'POST':
        username = request.form.get('username')
        phone = request.form.get('phone')
        pwd = request.form.get('pwd')
        repwd = request.form.get('repwd')

        if pwd == repwd:
            user = User(username, phone, pwd)
            userList.append(user)
            return redirect('/')
        else:
            return '密码不匹配'
    else:
        return render_template('user/register.html')


@userBp.route('/login', endpoint='login', methods=['POST', 'GET'])
def userLogin():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('pwd')

        for user in userList:
            if user.username == username:
                if user.password == password:
                    return 'Login success'
                else:
                    return 'Password Error'
        return redirect(url_for('user.login'))
    
    return render_template('user/login.html')