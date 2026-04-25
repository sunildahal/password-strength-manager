from flask import Flask
from auth.routes import auth_bp
from auth.models import bcrypt
from strength.routes import strength_bp
from generator.routes import generator_bp
from breach_check.routes import breach_bp
from activity_log.routes import dashboard_bp


app = Flask(__name__)
app.secret_key = "super-secret-key"

bcrypt.init_app(app)

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(strength_bp, url_prefix="/strength")
app.register_blueprint(generator_bp, url_prefix="/generator")
app.register_blueprint(breach_bp, url_prefix="/breach")
app.register_blueprint(dashboard_bp, url_prefix="/dashboard")



@app.route("/")
def home():
    return "Password Strength Manager API is running!"

if __name__ == "__main__":
    app.run(debug=True)
