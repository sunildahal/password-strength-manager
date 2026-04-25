from flask import Blueprint, request, jsonify
from .entropy import calculate_entropy
from .scoring import complexity_score
from .patterns import detect_patterns
from .dictionary_check import dictionary_attack
from activity_log.logger import log_action

strength_bp = Blueprint("strength", __name__)

@strength_bp.route("/check", methods=["POST"])
def check_strength():
    data = request.json
    password = data.get("password")

    if not password:
        return jsonify({"error": "Password is required"}), 400

    entropy = calculate_entropy(password)
    score = complexity_score(password)
    patterns = detect_patterns(password)
    dictionary_flag = dictionary_attack(password)

    log_action(user="anonymous", action="Checked password strength")
    return jsonify({
        "password": password,
        "entropy": entropy,
        "complexity_score": score,
        "patterns": patterns,
        "dictionary_weak": dictionary_flag
    })
