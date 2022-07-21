from .entities.usuario import Usuario

class ModelUsuario():

    @classmethod
    def login(self, db, usuario):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT * FROM user WHERE usuario = '{}' ".format(usuario['usuario'])
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                user = Usuario(row[0], row[1], usuario.Vcontra(row[2], usuario['contraseña']), row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, usuario, Nombre, Apellido FROM user WHERE id = {}".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                logged_user = Usuario(row[0], row[1], None, row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
                return logged_user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)