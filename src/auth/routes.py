from flask import Blueprint, request, session, jsonify
from .utils import verify_credentials, verify_2fa, get_role

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    valid, user = verify_credentials(username, password)
    if not valid:
        return jsonify({"error": "Invalid username or password"}), 401

    session["pending_user"] = username
    return jsonify({"message": "Password OK. Enter 2FA token."})

@auth_bp.route("/verify-2fa", methods=["POST"])
def verify_2fa_route():
    if "pending_user" not in session:
        return jsonify({"error": "No login session"}), 400

    username = session["pending_user"]
    token = request.json.get("token")

    user = users[username]
    if verify_2fa(user, token):
        session["user"] = username
        session["role"] = get_role(username)
        session.pop("pending_user")
        return jsonify({"message": "Login successful", "role": session["role"]})

    return jsonify({"error": "Invalid 2FA token"}), 401

@auth_bp.route("/logout")
def logout():
    session.clear()
    return jsonify({"message": "Logged out"})
