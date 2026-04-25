from flask import request
from .models import ActivityLog, activity_logs

def log_action(user, action):
    ip = request.remote_addr
    log = ActivityLog(user=user, action=action, ip=ip)
    activity_logs.append(log)
