from flask import Blueprint, request, jsonify
from .breach import check_pwned

breach_bp = Blueprint("breach", __name__)

@breach_bp.route("/check", methods=["POST"])
def breach_check():
    data = request.json
    password = data.get("password")

    if not password:
        return jsonify({"error": "Password is required"}), 400

    result = check_pwned(password)

    return jsonify(result)
