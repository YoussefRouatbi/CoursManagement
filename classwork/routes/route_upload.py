from flask import Blueprint, send_from_directory, jsonify, request,current_app
from werkzeug.utils import secure_filename
from connect_db import connect_database
import os

upload_content = Blueprint('upload_content',__name__)
allowed_ext = {'pdf'}

@upload_content.route('/upload_file', methods = ['POST'])
def upload_files():
    file = request.files['file']
    titleFile = request.form['title']
    subtitle = request.form['subtitle']
    matier = LoadMatier(request.form['matier'])

    if not file:
        return jsonify({'message':'No file selected'}),400
    if not allowed_file(file.filename):
        return jsonify({'message':'Invalid Document'}),400
    
    filename = secure_filename(file.filename)
    upload_folder = current_app.config['UPLOAD_FOLDER']
    file_path = os.path.join(upload_folder,filename)
    file.save(file_path)
    file_url = f'http://127.0.0.1:5000/courses/{filename}'
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO course(title,subtitle,file_path,file_url,idm) VALUES(%s,%s,%s,%s,%s)',(titleFile,subtitle,file_path,file_url,matier))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message' : 'course added successfully'}),200

@upload_content.route('/courses', methods = ['GET'])
def courses():
    conn = connect_database()
    matier = request.args.get('matier')
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM course as c, matier as m where c.idm = m.idm and m.nameMatier = %s',(matier,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(rows)

@upload_content.route('/courses/<path:filename>',methods = ['GET'])
def serve_cour(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'],filename)

def LoadMatier(matier):
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute('SELECT idm from matier where nameMatier = %s',(matier,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return row[0]

def allowed_file(filename:str):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in allowed_ext