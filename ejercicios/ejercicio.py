from peewee import AutoField, CharField, TextField
from usuarios.model import BaseModel


class Ejercicio(BaseModel):

    id_ejercicio = AutoField()
    nombre = TextField()
    descripcion = TextField()
    tipo = CharField(max_length = 9)

    def recuperarEjercicios(self):
    
        ejercicios = Ejercicio.select()

        return ejercicios