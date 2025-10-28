from flask import request, jsonify, Blueprint
from connect_db import connect_database


auth_user  = Blueprint('auth_user',__name__)

@auth_user.route('/login',methods = ['POST'])
def upload_user():
    username = request.form['username']
    password = request.form['password']
    if not username or not password:
        return jsonify({'message': 'Username and password required'}), 400
    conn = connect_database()
    cursor = conn.cursor()
    req = 'SELECT * FROM USERS WHERE username = %s and user_password = %s'
    cursor.execute(req,(username,password))
    rows = cursor.fetchall()
    if not rows:
        return jsonify({'message' : 'User not found'}),400
    else:
        return jsonify({'message' : 'User Loged in', 'username' : username}),200
