from flask import render_template, redirect, url_for, session, request
from app import app, google
from app.models.model import UsuarioModel

@app.route('/')
def index():
    model = UsuarioModel()
    usuarios = model.get_usuarios()
    return render_template('index.html', usuarios=usuarios)

@app.route('/login')
def login():
    return google.authorize(callback=url_for('authorized', _external=True))

@app.route('/google/callback')
def authorized():
    resp = google.authorized_response()
    if resp is None or resp.get('access_token') is None:
        return 'Acceso denegado: razón=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    session['google_token'] = (resp['access_token'], '')
    user_info = google.get('userinfo')
    return 'Usuario autenticado: ' + str(user_info.data)

@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')
