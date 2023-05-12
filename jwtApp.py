from flask import Flask, make_response
from flask import jsonify
from flask import request
from multiprocessing.dummy import current_process
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__, static_url_path='/static')

app.config["JWT_SECRET_KEY"] = "myjwtsecretkey"
app.config["JWT_TOKEN_LOCATION"] = ["headers", "cookies"] 
jwt = JWTManager(app)

account = {
    "username": "test",
    "password": "test"
}

@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    
    if username != account["username"] or password != account["password"]:
        return jsonify({"message": "Bad username or password"}), 401

    access_token = create_access_token(identity=account)
    response = make_response(jsonify(access_token=access_token), 200)
    response.set_cookie('access_token_cookie', access_token)
    return response

@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200

@app.route("/", methods=["GET"])
def mainPage():
    return 200

if __name__ == "__main__":
    app.run(port=5000)
