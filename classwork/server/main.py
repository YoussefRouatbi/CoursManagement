from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
import mysql.connector
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:5173"]}}, supports_credentials=True)

UPLOAD_FOLDER = 'course_files'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {'pdf'}

# --- Database connection ---
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="coursemanagement"
    )

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# --- Upload PDF endpoint ---
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    if not allowed_file(file.filename):
        return jsonify({'error': 'Only PDF files allowed'}), 400

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    file_url = f'http://127.0.0.1:5000/course_files/{filename}'

    return jsonify({'message': 'File uploaded', 'filename': filename, 'url': file_url}), 200

# --- Save course with matier ---
@app.route('/saveData', methods=['POST'])
def save_data():
    title = request.form.get('title')
    subtitle = request.form.get('subtitle', '')
    file_url = request.form.get('file')
    course_type = request.form.get('type', '')
    matier_name = request.form.get('matierName')

    if not title or not file_url or not matier_name:
        return jsonify({'error': 'Title, file, and matier required'}), 400

    conn = connect_db()
    cursor = conn.cursor()

    # Check if matier exists
    cursor.execute("SELECT idm FROM matier WHERE nameMatier=%s", (matier_name,))
    matier = cursor.fetchone()

    if matier:
        matier_id = matier[0]
    else:
        # Insert matier if it doesn't exist
        cursor.execute("INSERT INTO matier (nameMatier) VALUES (%s)", (matier_name,))
        matier_id = cursor.lastrowid

    # Insert course
    cursor.execute(
        "INSERT INTO course (title, subtitle, file_path, file_type) VALUES (%s, %s, %s, %s)",
        (title, subtitle, file_url, course_type)
    )
    course_id = cursor.lastrowid

    # Link course to matier
    cursor.execute("INSERT INTO matierCour (idm, idc) VALUES (%s, %s)", (matier_id, course_id))

    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({'message': 'Course saved successfully!'}), 200

# --- Serve uploaded files ---
@app.route('/course_files/<path:filename>')
def serve_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# --- Get courses with matier names ---
@app.route('/getCourses', methods=['GET'])
def get_courses():
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT c.idc, c.title, c.subtitle, c.file_path, c.file_type, m.nameMatier AS matier_name
        FROM course c
        JOIN matierCour mc ON c.idc = mc.idc
        JOIN matier m ON mc.idm = m.idm
        ORDER BY c.idc DESC
    """)
    courses = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(courses)

# --- Get all matiers ---
@app.route('/getMatiers', methods=['GET'])
def get_matiers():
    conn = connect_db()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM matier")
    matiers = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(matiers)

if __name__ == '__main__':
    app.run(debug=True)
