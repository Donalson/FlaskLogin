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
                user = Usuario(row[0], row[1], Usuario.Vcontra(row[2], usuario['contraseña']), row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10])
                return user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_by_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = "SELECT id, usuario, Nombre, Apellido, FNacimiento, Genero, Telefono, Foto, FC, FE FROM user WHERE id = {}".format(id)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row != None:
                logged_user = Usuario(row[0], row[1], None, row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9])
                return logged_user
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def registrar(self,db, usuario):
        try:
            cursor = db.connection.cursor()
            sql = """
            INSERT INTO `user`(`id`, `usuario`, `contraseña`, `Nombre`, `Apellido`, `FNacimiento`, `Genero`, `Telefono`, `Foto`, `FC`, `FE`)
            VALUES ('NULL','{}','{}','{}','{}','{}','{}','{}','NULL', current_timestamp(),'NULL')
            """.format(usuario['nombre'], Usuario.cifrar(usuario['contraseña']), usuario['nombre'], usuario['apellido'], usuario['fnacimiento'], usuario['genero', ])
            print(cursor.execute(sql))
            print(cursor.lastrowid)
            
        except Exception as ex:
            raise Exception(ex)