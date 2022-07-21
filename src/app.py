#Importaciones de paquetes/librerias y de otros archivos
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager, login_user, logout_user, login_required
from config import config

#Modelos
from models.ModelUsuario import ModelUsuario

#Entidades
from models.ModelUsuario import Usuario

#Se instancia la aplicacion de flask
app = Flask(__name__)
csrf = CSRFProtect()

#Conexion a base de datos y manejo de sesiones
db = MySQL(app)
login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUsuario.get_by_id(db,id)

#Rutas
@app.route("/")
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #print(request.form['usuario'])
        #print(request.form['contraseña'])
        #usuario = Usuario(0, request.form['usuario'], request.form['contraseña'], 'Donalson Static', None, None, None, None, None, None, None,)
        usuario = {'usuario': request.form['usuario'], 'contraseña': request.form['contraseña']}
        logged_user = ModelUsuario.login(db, usuario)
        if logged_user != None:
            if logged_user.contraseña:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash('Contraseña incorrecta...')    
                return render_template('auth/login.html')
        else:
            flash('Usuario o contraseña no encontrado...')    
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/registrar', methods=['POST'])
def registrar():
    if request.method == 'POST':
        usuario = {'usuario':request.form['usuarior'], 'contraseña':request.form['contraseñar'], 'nombre':request.form['nombrer'], 'apellido':request.form['apellidor'], 'fnacimiento':request.form['fnacimiento'], 'genero':request.form['genero'], 'telefono':request.form['telefonor']}
        user = ModelUsuario.registrar(db,usuario)
        print(user)
        return redirect(url_for('404'))
    else:
        flash('Algo salio mal con el registro')
        return render_template('auth/login.html')
        

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/home')
@login_required
def home():
    return render_template('home.html')

@app.route('/perfil')
@login_required
def perfil():
    return render_template('perfil.html')

def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return render_template('404.html')

#Se inicializa la aplicacion de flask y se le pasan algunos parametros
if __name__ == '__main__':
    app.config.from_object(config['development'])
    csrf.init_app(app)
    app.register_error_handler(401,status_401)
    app.register_error_handler(404,status_404)
    app.run()