from flask import request, jsonify, Blueprint, session
from connect_db import connect_database
from flask_cors import CORS


auth_user  = Blueprint('auth_user',__name__)

def is_logged_in():
    return 'username' in session

@auth_user.route('/login',methods = ['POST'])
def upload_user():
    username = request.form.get('username')
    password = request.form.get('password')
    if is_logged_in():
        return jsonify({'message':f"User {session['username']} already logged in"}), 200
    if not username or not password:
        return jsonify({'message': 'Username and password required'}), 400
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM USERS WHERE username = %s and user_password = %s',(username,password))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    if not rows:
        return jsonify({'message' : 'User not found'}),400
    session.permanent = True
    session['username'] = username
    print(session)
    return jsonify({'message' : 'User logged in successfully', 'username' : username}),200
