import pyotp
from flask_bcrypt import check_password_hash
from .models import users

def verify_credentials(username, password):
    if username not in users:
        return False, None

    stored_hash = users[username]["password"]
    if check_password_hash(stored_hash, password):
        return True, users[username]
    return False, None

def verify_2fa(user, token):
    totp = pyotp.TOTP(user["2fa_secret"])
    return totp.verify(token)

def get_role(username):
    return users[username]["role"]
