from flask_cors import CORS, cross_origin
from flask import Flask, jsonify, abort
from flask import request as flask_request
from linkProcessor import process
from functools import wraps
import jwt

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/api/blacklist', methods=['GET'])
@cross_origin()
def isBlacklisted():
    url = flask_request.args.get('url')
    return {'blacklisted':process(url)}

@app.route('/api/url-scan', methods=['GET'])
@cross_origin()
def scanUrl():
    url = flask_request.args.get('url')
    return {'blacklisted':process(url)}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=106)
    
    
    
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in flask_request.headers:
            token = flask_request.headers["Authorization"].split(" ")[1]
        if not token:
            return {
                "message": "Authentication Token is missing!",
                "data": None,
                "error": "Unauthorized"
            }, 401
        try:
            data=jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
            current_user=models.User().get_by_id(data["user_id"])
            if current_user is None:
                return {
                "message": "Invalid Authentication token!",
                "data": None,
                "error": "Unauthorized"
            }, 401
            if not current_user["active"]:
                abort(403)
        except Exception as e:
            return {
                "message": "Something went wrong",
                "data": None,
                "error": str(e)
            }, 500

        return f(current_user, *args, **kwargs)

    return decorated