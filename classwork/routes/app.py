from flask import Flask
from flask_cors import CORS
from route_Login import auth_user
from route_signup import auth_user_signup
from route_upload import upload_content
from me import me_bp
from admin import import_info
from datetime import timedelta
from dotenv import load_dotenv
import os
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days = 4)

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'courses')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config.update(
    SESSION_COOKIE_SAMESITE="None",
    SESSION_COOKIE_SECURE=True
)
CORS(app,origins="*",supports_credentials=True)


app.register_blueprint(auth_user)
app.register_blueprint(auth_user_signup)
app.register_blueprint(me_bp)
app.register_blueprint(upload_content)
app.register_blueprint(import_info)



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,debug=True)
