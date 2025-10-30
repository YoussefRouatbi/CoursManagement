from flask import Flask
from flask_cors import CORS
from route_Login import auth_user
from route_signup import auth_user_signup
from me import me_bp
from datetime import timedelta


app = Flask(__name__)
app.secret_key = "super_secret_key"
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days = 4)

app.config.update(
    SESSION_COOKIE_SAMESITE="None",
    SESSION_COOKIE_SECURE=False
)
CORS(app,supports_credentials=True)


app.register_blueprint(auth_user)
app.register_blueprint(auth_user_signup)
app.register_blueprint(me_bp)



if __name__ == '__main__':
    app.run(debug=True)
