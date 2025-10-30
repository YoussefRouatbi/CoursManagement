from flask import Flask
from flask_cors import CORS
from route_Login import auth_user
from route_signup import auth_user_signup
from route_upload import upload_content
from me import me_bp
from datetime import timedelta
import os


app = Flask(__name__)
app.secret_key = "b7bc4ec03115df426f9fb29bdb7bf3feb90fbc144f74afc25684b909fe783f6e"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days = 4)

UPLOAD_FOLDER = os.path.join(os.getcwd(), 'courses')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config.update(
    SESSION_COOKIE_SAMESITE="None",
    SESSION_COOKIE_SECURE=True
)
CORS(app,supports_credentials=True)


app.register_blueprint(auth_user)
app.register_blueprint(auth_user_signup)
app.register_blueprint(me_bp)
app.register_blueprint(upload_content)



if __name__ == '__main__':
    app.run(debug=True)
