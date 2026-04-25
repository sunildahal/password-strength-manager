from flask import Flask
from auth.routes import auth_bp
from auth.models import bcrypt
from strength.routes import strength_bp
from generator.routes import generator_bp
from breach_check.routes import breach_bp
from activity_log.routes import dashboard_bp
from flask_swagger_ui import get_swaggerui_blueprint


app = Flask(__name__)
app.secret_key = "super-secret-key"

bcrypt.init_app(app)

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(strength_bp, url_prefix="/strength")
app.register_blueprint(generator_bp, url_prefix="/generator")
app.register_blueprint(breach_bp, url_prefix="/breach")
app.register_blueprint(dashboard_bp, url_prefix="/dashboard")

# Swagger UI configuration
SWAGGER_URL = '/docs'
API_URL = '/static/swagger.yaml'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Password Strength Manager API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)



@app.route("/")
def home():
    return "Password Strength Manager API is running!"

if __name__ == "__main__":
    app.run(debug=True)
