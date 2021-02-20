from peewee import Model, MySQLDatabase


#----------------------- Conexión a la base de datos ---------------------------


def conexion():

    data_base = "pi_docker"
    host = "localhost"
    port = 3306
    username = "admin"
    password = "secreto"

    db = MySQLDatabase(
        data_base,
        host = host,
        port = port,
        user = username,
        password = password
        )

    return db


#------------------------- Creación de entidades -------------------------------

class BaseModel(Model):
    class Meta:
        database = conexion()