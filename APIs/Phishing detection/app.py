from flask_cors import CORS, cross_origin
from flask import Flask, jsonify, abort
from flask import request as flask_request
from urlProcessor import predict, predictNlp
from functools import wraps
# import jwt

app = Flask(__name__)
CORS(app, support_credentials=True)

map = {
    -1:True,
    1:False
}

def mapBlacklist(x):
    return x == -1

def mapSpam(x):
    return x == "spam"

@app.route('/api/process-url', methods=['GET'])
@cross_origin()
def processUrl():
    url = flask_request.args.get('url')
    res = predict(url)[0]
    # print(res)
    return {'spam':bool(mapBlacklist(res))}

@app.route('/api/process-nlp', methods=['POST'])
@cross_origin()
def processNlp():
    text = flask_request.json['text']
    return {'spam':mapSpam(predictNlp([text])[0])}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=107)
    
    
    
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