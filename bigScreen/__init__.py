# coding: utf-8
# author: chaney
# time  : 2024-06-28
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    # 1.从settings.py中读取配置
    app.config.from_object('settings.DevelopmentConfig')

    # 2. 注册蓝图
    from bigScreen.views import user
    app.register_blueprint(user.bp)

    with app.app_context():
        # 初始化数据库
        db.init_app(app)
        # 删除所有表
        db.drop_all()
        # 创建表
        db.create_all()

    return app
