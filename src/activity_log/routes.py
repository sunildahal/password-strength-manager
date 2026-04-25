from flask import Blueprint, jsonify
from .models import activity_logs

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/logs", methods=["GET"])
def get_logs():
    return jsonify([log.to_dict() for log in activity_logs])
