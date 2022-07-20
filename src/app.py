#Importaciones de paquetes/librerias y de otros archivos
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from config import config

#Se instancia la aplicacion de flask
app = Flask(__name__)

#Conexion a base de datos
db = MySQL(app)

#Rutas
@app.route("/")
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print(request.form['usuario'])
        print(request.form['contraseña'])
        return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

#Se inicializa la aplicacion de flask y se le pasan algunos parametros
if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()