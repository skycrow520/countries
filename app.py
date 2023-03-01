from flask import Flask, request, jsonify
from user import User

from db import DataBase

import os

app = Flask(__name__)
db = DataBase(os.getenv('SQL_HOST_IP'), 3306, 'root', os.getenv('SQL_ROOT_PASSWD'), 'countries', 'utf8')

loginned_users = {}

@app.route('/login')
def login():
    uid = request.args.get('uid')
    if uid:
        user_obj = User(data=db, uid=uid)
        loginned_users[f'{uid}'] = user_obj
        return jsonify
