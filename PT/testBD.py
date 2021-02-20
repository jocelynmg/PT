from peewee import *
import os

"""
-------- Este script sólo se deberá ejecutar para crear la base de datos -------
"""

data_base = "pi_docker"
host = "localhost"
port = 3306
username = "admin"
password = "secreto"

#--------------- Crea la base de datos en el servidor --------------------------

os.system("echo \"create database if not exists "+data_base+";\" | mysql --user="
                                            +username+" --password="+password)


#----------------------- Conexión a la base de datos ---------------------------

db = MySQLDatabase(
    data_base,
    host = host,
    port = port,
    user = username,
    password = password
    )

#------------------------- Creación de entidades -------------------------------

class BaseModel(Model):
    class Meta:
        database = db

class Usuario(BaseModel):
    id_usuario = AutoField()
    nombre = CharField(max_length = 30)
    username = CharField(max_length = 15, unique = True)
    password = CharField(max_length = 64)

class Ejercicio(BaseModel):
    id_ejercicio = AutoField()
    nombre = TextField()
    descripcion = TextField()
    tipo = CharField(max_length = 9)

class Avance_Usuario(BaseModel):
    id_avance = AutoField()
    usuario = ForeignKeyField(Usuario, backref = 'avance')
    ejercicio = ForeignKeyField(Ejercicio, backref = 'avance')
    resuelto = BooleanField()
    intento = SmallIntegerField()
"""
class Comando_Preparacion(BaseModel):
    id_preparacion = AutoField()
    comando = TextField()
    orden = IntegerField()
    ejercicio = ForeignKeyField(Ejercicio, backref = 'comando_preparacion')

class Comando_Evaluacion(BaseModel):
    id_evaluacion = AutoField()
    comando = TextField()
    orden = IntegerField()
    ejercicio = ForeignKeyField(Ejercicio, backref = 'comando_evaluacion')
"""


#------------------- Crea las tablas en la base de datos -----------------------


db.connect()

db.create_tables([
    Usuario,
    Ejercicio,
    Avance_Usuario,
#    Comando_Preparacion,
#    Comando_Evaluacion
    ])

db.close()
