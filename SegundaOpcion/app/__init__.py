from flask import Flask
from flask_login import LoginManager
from .models.user import User
from .controllers.auth_controller import auth
from .controllers.appointment_controller import appointment
from .views.views import main

app = Flask(__name__)
app.config.from_object('config.Config')

# Configuración de la base de datos
# db.init_app(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get_user_by_id(user_id)

app.register_blueprint(auth)
app.register_blueprint(appointment, url_prefix='/appointment')
app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)
