from flask import Flask
from auth.routes import auth_bp
from auth.models import bcrypt

app = Flask(__name__)
app.secret_key = "super-secret-key"  # Replace with secure key

bcrypt.init_app(app)

app.register_blueprint(auth_bp, url_prefix="/auth")

@app.route("/")
def home():
    return "Password Strength Manager API is running!"

if __name__ == "__main__":
    app.run(debug=True)
