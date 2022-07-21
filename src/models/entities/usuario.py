from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin

class Usuario(UserMixin):

    def __init__(self, id, usuario, contraseña, nombre, apellido, fnacimiento, genero, telefono, foto, fc, fe) -> None:
        pass
        self.id = id
        self.usuario = usuario
        self.contraseña = contraseña
        self.nombre = nombre
        self.apellido = apellido
        self.fnacimiento = fnacimiento
        self.genero = genero
        self.telefono = telefono
        self.foto = foto
        self.fc = fc
        self.fe = fe

    @classmethod
    def Vcontra(self, contra_hasheada, contraseña):
        return check_password_hash(contra_hasheada,contraseña)

    @classmethod
    def cifrar(contra):
        return generate_password_hash(contra)