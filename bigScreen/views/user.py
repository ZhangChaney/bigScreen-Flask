# coding: utf-8
# author: chaney
# time  : 2024/6/28
from flask import Blueprint, request, session

from bigScreen.models import *
from bigScreen.common import *

# 分模块划分蓝图，用户相关接口均以/user路由开头
bp = Blueprint('user', __name__, url_prefix='/user')


@bp.post('/login')
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


@bp.post('/auth')
def auth():
    # 检查请求是否携带session中的username
    if not session.get('username'):
        # session里面有用户信息
        return Result.error(message='请先登录！')

    return Result.success()


# CRUD
# 添加数据 RestFul  post 增 get 查 delete删  put 改
@bp.post('/add')
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


@bp.put('/update')
def update_user():
    # 先获取传递过来的 参数，需要修改的信息
    password = request.get_json()['password']
    username = request.get_json().get('username')
    userid = request.get_json().get('userid')
    phone = request.get_json().get('phone')
    email = request.get_json().get('email')
    role = request.get_json().get('role')
    # 根据userid查询用户
    u = User.query.get(userid)
    if u:
        u.username = username
        u.password = password
        u.phone = phone
        u.email = email
        u.role = role
    try:
        db.session.commit()
        return Result.success(message='更新成功！')
    except Exception as e:
        db.session.rollback()
        print(e)
        return Result.error(message="用户不存在！")


@bp.delete('/delete/<int:user_id>')
def delete_user(user_id: int):
    try:
        User.query.filter(User.userid == user_id).delete()
        db.session.commit()
        return Result.success(message='删除成功!')
    except Exception as e:
        db.session.rollback()
        print(e)
        return Result.error(message='删除失败！')


@bp.get('/getAll')
def get_all_user():
    users = User.query.all()
    # 返回的是一个有所有用户对象的列表, 列表元素都是对象
    # 因为对象不能直接json化返回给前端 会报下面错误
    # Object of type User is not JSON serializable
    # 遍历每一个对象，全部转成字典后添加到一个列表里，让后将这个列表返回给前端
    # 因为列表是可以json化的
    data = []
    for user in users:
        data.append(user.to_dict())

    return Result.success(data=data)


@bp.get('/getUserById/<int:user_id>')
def get_user_by_id(user_id: int):
    user = User.query.filter_by(userid=user_id).first()
    if not user:
        return Result.error(message='用户不存在！')
    return Result.success(data=user.to_dict())
