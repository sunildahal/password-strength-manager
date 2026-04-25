from flask import Blueprint, request, session, jsonify, redirect, url_for, flash
from .utils import verify_credentials, verify_2fa, get_role
from .models import users
from activity_log.logger import log_action

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    if request.is_json:
        # API request
        data = request.json
        username = data.get("username")
        password = data.get("password")

        valid, user = verify_credentials(username, password)
        if not valid:
            return jsonify({"error": "Invalid username or password"}), 401

        session["pending_user"] = username
        return jsonify({"message": "Password OK. Enter 2FA token."})
    else:
        # Form submission
        username = request.form.get("username")
        password = request.form.get("password")

        valid, user = verify_credentials(username, password)
        if not valid:
            flash("Invalid username or password", "error")
            return redirect(url_for("login_page"))

        session["pending_user"] = username
        return redirect(url_for("login_page"))  # Will show 2FA form via JS

@auth_bp.route("/verify-2fa", methods=["POST"])
def verify_2fa_route():
    if "pending_user" not in session:
        if request.is_json:
            return jsonify({"error": "No login session"}), 400
        else:
            flash("No login session", "error")
            return redirect(url_for("login_page"))

    username = session["pending_user"]
    token = request.json.get("token") if request.is_json else request.form.get("token")

    user = users[username]
    if verify_2fa(user, token):
        session["user"] = username
        session["role"] = get_role(username)
        session.pop("pending_user")
        log_action(user=username, action="User logged in")

        if request.is_json:
            return jsonify({"message": "Login successful", "role": session["role"]})
        else:
            flash("Login successful!", "success")
            return redirect(url_for("dashboard"))
    else:
        if request.is_json:
            return jsonify({"error": "Invalid 2FA token"}), 401
        else:
            flash("Invalid 2FA token", "error")
            return redirect(url_for("login_page"))

@auth_bp.route("/logout")
def logout():
    session.clear()
    if request.is_json:
        return jsonify({"message": "Logged out"})
    else:
        flash("Logged out successfully", "info")
        return redirect(url_for("dashboard"))
