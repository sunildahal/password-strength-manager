from datetime import datetime

activity_logs = []  # In-memory list (simple for assignment)

class ActivityLog:
    def __init__(self, user, action, ip):
        self.user = user
        self.action = action
        self.ip = ip
        self.timestamp = datetime.utcnow()

    def to_dict(self):
        return {
            "user": self.user,
            "action": self.action,
            "ip": self.ip,
            "timestamp": self.timestamp.isoformat() + "Z"
        }
