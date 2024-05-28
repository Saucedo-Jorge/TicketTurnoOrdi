from flask import Flask
from flask_login import LoginManager
from .models.user import User
from .models.db import db

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    from .controllers.auth_controller import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .controllers.appointment_controller import appointment as appointment_blueprint
    app.register_blueprint(appointment_blueprint)

    from .views.views import main as main_blueprint
    app.register_blueprint(main_blueprint)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE idusers = %s", (user_id,))
        user_data = cursor.fetchone()
        cursor.close()
        if user_data:
            return User(user_data['idusers'], user_data['username'], user_data['password'])
        return None

    return app
