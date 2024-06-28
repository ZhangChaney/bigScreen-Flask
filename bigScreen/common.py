# coding: utf-8
# author: chaney
# file  : common.py
# time  : 2024-06-19
class Result:
    #  返回类型一般就两种：成功或者失败
    #  成功code为1，失败为-1
    @staticmethod
    def success(code=1, message='操作成功！', data=None):
        return {'code': code, 'message': message, 'data': data}

    @staticmethod
    def error(code=-1, message='操作失败！', data=None):
        return {'code': code, 'message': message, 'data': data}

