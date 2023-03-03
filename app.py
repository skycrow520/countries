from flask import Flask, request, jsonify
from user import User

from db import DataBase

import os

app = Flask(__name__)
db = DataBase(os.getenv('SQL_HOST'), os.getenv('SQL_PORT'), os.getenv('SQL_USER'), os.getenv('SQL_PASSWD'), 'game', 'utf8')

loginned_users = {}

@app.route('/login')
def login():
    uid = request.args.get('uid')
    if uid:
        user_obj = User(data=db, uid=uid)
        loginned_users[f'{uid}'] = user_obj
        return jsonify
