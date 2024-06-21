# coding: utf-8
# author: chaney
# file  : app.py
# time  : 2024-06-19
from flask import Flask, request, session
from flask_sqlalchemy import SQLAlchemy

from model.common import Result

app = Flask(__name__)

app.config['SECRET_KEY'] = '136-588-342'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@1.95.59.210:3321/class0102'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64), unique=True)
    phone = db.Column(db.String(11), unique=True)
    email = db.Column(db.String(64), unique=True)

    def __init__(self, username=None, password=None, phone=None, email=None):
        self.username = username
        self.password = password
        self.phone = phone
        self.email = email

    def __repr__(self):
        return f'<User {self.username!r}>'

    def to_dict(self):
        return {
            'userid': self.userid,
            'username': self.username,
            'phone': self.phone,
            'email': self.email
        }


# 视图函数
@app.route('/user/login', methods=['post'])
def login():
    password = request.get_json()['password']
    username = request.get_json().get('username')

    u = User.query.filter_by(username=username, password=password).first()
    if u:  # 非空即存在该用户，校验成功
        session['userid'] = u.userid
        session['username'] = u.username
        return Result.success(data=u.to_dict())
    # 登录失败
    return Result.error()


@app.route('/auth', methods=['post'])
def auth():
    # 检查请求是否携带session中的username
    if not session.get('username'):
        # session里面有用户信息
        return Result.error(message='请先登录！')

    return Result.success()


# CRUD
# 添加数据 RestFul  post 增 get 查 delete删  put 改
@app.route('/user/add', methods=['post'])
def add_user():
    password = request.get_json()['password']
    username = request.get_json().get('username')
    phone = request.get_json().get('phone')
    email = request.get_json().get('email')
    u = User(
        username=username, password=password,
        phone=phone, email=email
    )
    db.session.add(u)
    db.session.commit()

    return Result.success()


@app.route('/user/update', methods=['put'])
def update_user():
    # 先获取传递过来的 参数，需要修改的信息
    password = request.get_json()['password']
    username = request.get_json().get('username')
    userid = request.get_json().get('userid')
    # 根据userid查询用户
    u = User.query.get(userid)
    if u:
        u.username = username
        u.password = password
        db.session.commit()
        return Result.success()
    return Result.error(message="用户不存在！")


@app.route('/user/getAll', methods=['get'])
def get_all_user():
    users = User.query.all()  # 返回的是一个有所有用户对象的列表, 列表元素都是对象
    # 因为对象不能直接json化返回给前端 会报下面错误
    # Object of type User is not JSON serializable
    # 遍历每一个对象，全部转成字典后添加到一个列表里，让后将这个列表返回给前端
    # 因为列表是可以json化的
    data = []
    for user in users:
        data.append(user.to_dict())

    return Result.success(data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
