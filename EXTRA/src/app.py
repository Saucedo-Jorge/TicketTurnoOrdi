from flask import Flask, flash, redirect, render_template, request, url_for
from config import config
from flask_mysqldb import MySQL

from models.ModelUser import ModelUser
from models.entities.User import User

app = Flask(__name__)

db = MySQL(app)

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/sign', methods=['GET', 'POST'])
def sign():
    if request.method == 'POST':  
        
        user = User(0,request.form['username'],request.form['password'])
        logged_user = ModelUser.login(db,user)
        if logged_user != None:
            if logged_user.password:
                return redirect(url_for('home'))
            else:
                flash('Contraseña incorrecta')
                return render_template('auth/login.html')
        else:
            flash('Usuario no encontrado')
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')
    
@app.route('/home')
def home():
    return render_template('views/index.html')




if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run(port=4322)