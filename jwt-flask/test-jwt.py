from flask import Flask, request, jsonify
import jwt
import datetime

app = Flask(__name__)

app.config["SECRET_KEY"] = "my_secret_key"

users = {
    "testuser": "password123"
}

@app.route("/login", methods=['POST'])
def login():
    auth = request.json
    if not auth or not auth.get('username') or not auth.get('password'):
        return jsonify({'message': 'Could not verify'}), 401
    
    username = auth.get("username")
    password = auth.get("password")
    
    if username in users and users[username] == password:
        token = jwt.encode({
            "username": username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, app.config["SECRET_KEY"], algorithm="HS256")
        return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials'}), 403

@app.route('/protected', methods=['GET'])
def protected():
    token = request.headers.get('x-access-token')
    if not token:
        return jsonify({"message": "Token is missing"}), 401
    
    try:
        data = jwt.decode(token, app.config["SECRET_KEY"], algorithms=['HS256'])
        current_user = data["username"]
    except jwt.ExpiredSignatureError:
        return jsonify({"message": "Token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"message": "Token is invalid"}), 401
    
    return jsonify({"message": f"Hello {current_user}!"})

if __name__ == "__main__":
    app.run(debug=True)