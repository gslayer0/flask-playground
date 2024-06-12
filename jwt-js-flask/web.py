from flask import Flask, render_template, url_for, request, jsonify, make_response, g
import jwt
import datetime

app = Flask(__name__)
app.config["SECRET_KEY"] = "my_secret_key"

users = {
    "user1": "password1",
    "user2": "password2"
}

data = {
    "user1": {"hobby": "playing football", "job": "programmer"},
    "user2": {"hobby": "running", "job": "accountant"},
}

def token_is_valid(func):
    def decorator(*args, **kwargs):
        token = request.cookies.get('token')
        if not token:
            return jsonify({"message": "Token is missing"}), 401
        try:
            data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=['HS256'])
            g.user = data["username"]
            return func(*args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify({"message": "Token has expired"}), 401
        except jwt.InvalidTokenError:
            return jsonify({"message": "Token is invalid"}), 401
    return decorator


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    req = request.json
    if not req or not req.get("name") or not req.get("password"):
        return jsonify({"message": "Formulir tidak lengkap"}), 400
    username = req.get("name")
    password = req.get("password")
    
    if username not in users or users[username] != password:
        return jsonify({"message": "username/sandi salah"}), 403
    
    token = jwt.encode({
        "username": username,
        "exp": datetime.datetime.now(datetime.UTC) + datetime.timedelta(seconds=30)
    }, app.config["SECRET_KEY"], algorithm="HS256")
    resp = make_response(jsonify({"message": "Login successful"}), 200)
    resp.set_cookie("token", token);
    return resp;

@app.route("/check", methods=["GET"])
@token_is_valid
def check():
    if g.user not in data:
        return jsonify({"message": "User tidak ditemukan"}), 400
    return jsonify({ "data": data[g.user]}), 200

if __name__ == "__main__":
    app.run(debug=True)