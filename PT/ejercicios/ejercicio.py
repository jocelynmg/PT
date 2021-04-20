from peewee import AutoField, CharField, TextField
from usuarios.model import BaseModel


class Ejercicio(BaseModel):

    id_ejercicio = AutoField()
    nombre = TextField()
    descripcion = TextField()
    tipo = CharField(max_length = 9)

    def recuperarEjercicios(self, tipo):
        """Se recuperan los ejercicios de la Base de datos"""
    
        #SE OBTIENEN LOS EJERCICIOS DE LA BD
        ejercicios = Ejercicio.select()
        #SE FILTRAN LOS EJERCICIOS POR TIPO
        listEjercicios = [e for e in ejercicios if e.tipo == tipo]

        return listEjercicios