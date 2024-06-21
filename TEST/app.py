# coding: utf-8
# author: chaney
# file  : app.py
# time  : 2024-06-19
from datetime import timedelta

from flask import Flask, session, request

from model.common import Result

app = Flask(__name__)
app.config['SECRET_KEY'] = '136-588-342'
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=30)


@app.route('/login', methods=['POST'])
def login():
    username = request.get_json().get('username')
    password = request.get_json().get('password')
    session['username'] = username

    return Result.success()


@app.route('/auth', methods=['POST'])
def auth():
    if session.get('username'):
        return Result.success()
    return Result.error()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
