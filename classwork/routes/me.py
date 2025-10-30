from flask import session, Blueprint,jsonify
from flask_cors import CORS

me_bp = Blueprint('me_bp',__name__)

@me_bp.route('/me',methods = ['GET'])
def me():
    if 'username' in session:
        return jsonify({'username': session['username']}), 200
    print(session)
    return jsonify({'username':None}), 401