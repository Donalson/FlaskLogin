#Importaciones de paquetes/librerias y de otros archivos
from flask import Flask
from config import config

#Se instancia la aplicacion de flask
app = Flask(__name__)

#Se inicializa la aplicacion de flask y se le pasan algunos parametros
if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()