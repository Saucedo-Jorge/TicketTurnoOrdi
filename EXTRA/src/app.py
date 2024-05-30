from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required

from config import config
from database import Database


# Models:
from factories import EntityFactory
from models.ModelUser import ModelUser
from models.ModelCita import ModelCita
from models.ModelAlumno import ModelAlumno
from models.ModelMunicipio import ModelMunicipio
from models.ModelDetalleCita import ModelDetalleCita

# Entities:
from models.entities.User import User

app = Flask(__name__)

csrf = CSRFProtect()
db = Database(app)
login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(user_id):
    return ModelUser.get_by_id(db, user_id)

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user is not None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Invalid password...")
                return render_template('auth/login.html')
        else:
            flash("User not found...")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template('views/index.html')

@app.route('/protected')
@login_required
def protected():
    return "<h1>Esta es una vista protegida, solo para usuarios autenticados.</h1>"


@app.route('/consulta_cita', methods=['POST', 'GET'])
def consulta_cita():
    if request.method == 'POST':
        numturno = request.form['numeroturno']
        curp = request.form['curp']
        phone = request.form['phone']
        email = request.form['email']
        asuntotratar = request.form['asuntotratar']
        statu= request.form['status']if 'status' in request.form and request.form['status'] else None
        connection = db.get_connection()
        cursor = connection.cursor()            
            
        sql =  """select c.TELEFONOQR, c.CORREOQR, r.asuntotratar, c.status from realiza r join citas c 
                        ON r.IDCITA = c.IDCITA where r.NUMTURNO = '{}' AND r.CURP = '{}';""".format( numturno,curp)
        cursor.execute(sql)
        data = cursor.fetchone()
        cu=curp
        nt=numturno
        num=data[0]
        correo=data[1]
        ast=data[2]
        sta=data[3]
    
        # Pasar los datos al template
        return render_template('views/ConsultaCita.html', cu=cu ,nt=nt, ast=ast, num=num, correo=correo)

    else:
        
        return render_template('views/ConsultaCita.html', data={})
    
@app.route('/modificar_cita', methods=['POST'])
def modificar_cita():
    if request.method == 'POST':
        
        curp = request.form['curp']
        phone = request.form['phone']
        email = request.form['email']
        asuntotratar = request.form['asuntotratar']
        statu= request.form['status']if 'status' in request.form and request.form['status'] else None

        connection = db.get_connection()
        cursor = connection.cursor()
        sql = "SELECT IDCITA, QUIENR, TELEFONOQR, CORREOQR, STATUS FROM citas"
        cursor.execute(sql)
        result = cursor.fetchall()
        citas = []
        for row in result:
            citas.append((row[0], row[1], row[2], row[3], row[4]))
        
        
        
        return redirect(url_for('consulta_cita'))
    else:
        return render_template('views/ConsultaCita.html')

@app.route('/eliminar_cita', methods=['POST'])
def eliminar_cita():
    if request.method == 'POST':
        numturno = request.form['numeroturno']
        curp = request.form['curp']

        d = EntityFactory.create_entity('detallecita', None, curp, numturno, None)
        ModelDetalleCita.delete_data(db, d)

        flash('Cita eliminada exitosamente', 'success')
        return redirect(url_for('consulta_cita'))
    else:
        return render_template('views/ConsultaCita.html', data={})


@app.route('/registro_cita', methods=['POST', 'GET'])
def registro_cita():
    if request.method == 'POST':
        quienr = request.form['quien']
        telefonoqr = request.form['phone']
        correo = request.form['email']
        statu= request.form['status']if 'status' in request.form and request.form['status'] else None
        
        
    
        cita = EntityFactory.create_entity('cita', None, quienr, telefonoqr, correo, statu)
        ModelCita.add(db, cita)
    
        curp= request.form['curp']
        asunto= request.form['asuntotratar']
        idcita= ModelCita.get_id(db)
        numcita=  ModelDetalleCita.numturn(db, curp)
        detalle = EntityFactory.create_entity('detallecita', idcita[0], curp, numcita, asunto)
        ModelDetalleCita.add(db, detalle)
        
        flash("Guarde su numero de Turno")
        flash(f"Turno Asignato: {numcita}")
        
        return redirect(url_for('registro_cita'))
    else:
        return render_template('views/registro_cita.html')

@app.route('/municipios')
@login_required
def municipios():
    return render_template('views/municipios.html')

@app.route('/alumnos')
@login_required
def alumnos():
    return render_template('views/alumnos.html')





@app.route('/about')
def about():
    return render_template('views/about.html')

def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return "<h1>Página no encontrada</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401, status_401)
    app.register_error_handler(404, status_404)
    app.run(port=4322)
