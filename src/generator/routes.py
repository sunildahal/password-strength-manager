from flask import Blueprint, request, jsonify
from .generator import generate_password

generator_bp = Blueprint("generator", __name__)

@generator_bp.route("/create", methods=["POST"])
def create_password():
    data = request.json or {}

    length = data.get("length", 12)
    use_upper = data.get("use_upper", True)
    use_lower = data.get("use_lower", True)
    use_digits = data.get("use_digits", True)
    use_symbols = data.get("use_symbols", True)

    password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)

    if not password:
        return jsonify({"error": "No character types selected"}), 400

    return jsonify({
        "generated_password": password,
        "length": length,
        "options": {
            "upper": use_upper,
            "lower": use_lower,
            "digits": use_digits,
            "symbols": use_symbols
        }
    })
