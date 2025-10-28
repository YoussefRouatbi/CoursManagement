from flask import Flask, request, jsonify, send_from_directory
from werkzeug.utils import secure_filename
from flask_cors import CORS
import os
from connect_db import connect_database


app  = Flask(__name__)
CORS(app)

@app.route('/login',methods = ['POST'])
def upload_user():
    username = request.form['username']
    password = request.form['password']
    conn = connect_database()
    cursor = conn.cursor()
    req = 'SELECT * FROM USERS WHERE username = %s and user_password = %s'
    cursor.execute(req,(username,password))
    rows = cursor.fetchall()
    if not rows:
        return jsonify({'message' : 'User not found'}),400
    else:
        return jsonify({'message' : 'User Loged in', 'username' : username}),200

if '__main__' == __name__:
    app.run(debug = True)