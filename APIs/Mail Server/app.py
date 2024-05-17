from flask_cors import CORS, cross_origin
from flask import Flask, jsonify, abort
from flask import request as flask_request
from server import getMessages, getMessagesAfter
from functools import wraps
import jwt
import json

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route('/api/emails', methods=['GET'])
@cross_origin()
def getEmails():
    data = flask_request.args.get('timestamp')
    if data: return app.response_class(
    response=getMessagesAfter(data),
    status=200,
    mimetype='application/json'
    )
    else: return app.response_class(
    response=getMessages(data),
    status=200,
    mimetype='application/json'
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)
    
    
    
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