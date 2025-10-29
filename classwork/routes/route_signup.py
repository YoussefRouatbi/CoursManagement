from flask import Blueprint, request, jsonify
from flask_cors import CORS
from connect_db import connect_database

auth_user_signup = Blueprint('auth_user_signup', __name__)

@auth_user_signup.route('/signup',methods = ['POST'])
def AddUser():
    username = request.form.get('username')
    password = request.form.get('password')
    if not username or not password:
        return jsonify({'message':'Username and password required'}),400
    if Upload_User(username):
        return jsonify({'message':'Username already exist'}),400
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users(username,user_password) VALUES(%s,%s)',(username,password))
    conn.commit()
    cursor.close()
    return jsonify({'message':'Account created successfully! You can now log in.'})

def Upload_User(username):
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute('SELECT 1 FROM users WHERE username = %s', (username,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    if not rows:
        return False
    return True

