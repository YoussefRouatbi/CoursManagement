from flask import Blueprint, request, jsonify
from flask_cors import CORS
from connect_db import connect_database

import_info = Blueprint('import_info',__name__)
CORS(import_info)

@import_info.route('/import', methods = ['GET'])
def loadData():
    users = upload_users()
    nb_users = len(users)
    course = upload_cousre()
    nb_course = len(course)
    return jsonify({'users' : users, 'course' : course, 'nbUsers' : nb_users, 'nbCourse' : nb_course})

@import_info.route("/")
def homepage():
    views = increment_views()
    return jsonify({'views' : views})

@import_info.route('/delete',methods = ['POST'])
def delete():
    title = request.form['title']
    fileUrl = request.form['fileUrl']
    if not title or not fileUrl:
        return jsonify({'message': 'title and file select required to delete'}), 400
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute('delete from course where title = %s and file_url = %s',(title, fileUrl))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message' : 'File removed succesfuly'}),200


def upload_users():
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute('SELECT username, typeUser, date_insc FROM users')
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def upload_cousre():
    conn = connect_database()
    cursor = conn.cursor()
    cursor.execute('SELECT title, file_url FROM course')
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows



counter_file = "views.txt"
def get_views():
    try:
        with open(counter_file, "r") as f:
            return int(f.read())
    except FileNotFoundError:
        return 0

def increment_views():
    count = get_views() + 1
    with open(counter_file, "w") as f:
        f.write(str(count))
    return count



