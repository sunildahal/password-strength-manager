import secrets
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    charset = ""

    if use_lower:
        charset += string.ascii_lowercase
    if use_upper:
        charset += string.ascii_uppercase
    if use_digits:
        charset += string.digits
    if use_symbols:
        charset += "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|"

    if not charset:
        return None  # No character types selected

    return ''.join(secrets.choice(charset) for _ in range(length))
