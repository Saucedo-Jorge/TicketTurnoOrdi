from flask import Flask
from flask_login import LoginManager
from .models.user import User

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Inicializar Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'

    from .controllers.auth_controller import auth as auth_blueprint
    from .controllers.appointment_controller import bp as appointment_blueprint
    from .views.views import bp as views_blueprint

    app.register_blueprint(auth_blueprint)
    app.register_blueprint(appointment_blueprint)
    app.register_blueprint(views_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.get_by_id(user_id)

    return app
