from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

# Temporary in-memory user store (replace with DB later)
users = {
    "admin": {
        "password": bcrypt.generate_password_hash("Admin@123").decode(),
        "role": "admin",
        "2fa_secret": "JBSWY3DPEHPK3PXP"  # Example secret
    },
    "user": {
        "password": bcrypt.generate_password_hash("User@123").decode(),
        "role": "user",
        "2fa_secret": "KZXW6YTBON2XEZJO"
    }
}
