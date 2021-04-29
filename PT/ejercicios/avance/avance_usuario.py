from peewee import AutoField, CharField, ForeignKeyField, BooleanField, SmallIntegerField
from usuarios.model import BaseModel
from usuarios.usuario import Usuario
from ejercicios.ejercicio import Ejercicio

class Avance_Usuario(BaseModel):
    id_avance = AutoField()
    usuario = ForeignKeyField(Usuario, backref = 'avance')
    ejercicio = ForeignKeyField(Ejercicio, backref = 'avance')
    resuelto = BooleanField(default = False)
    intento = SmallIntegerField(default = 0)


    def recuperarAvance(self, ejercicio, usuario):
        """En esta función se recuperan los avances del usuario"""

        id_usuario = usuario.id_usuario
        id_ejercicio = ejercicio.id_ejercicio

        try:
            avance = (Avance_Usuario
                    .select(Avance_Usuario)
                    .where(
                        Avance_Usuario.usuario == id_usuario, 
                        Avance_Usuario.ejercicio == id_ejercicio)
                    .get()
                    ) 

        except:
            avance = "No se encontraron registros"
        return avance


    def actualizarAvance(self, ejercicio, usuario, resultado):
        """Esta función actualizará los avances del usuarios"""

        id_usuario = usuario.id_usuario
        id_ejercicio = ejercicio.id_ejercicio

        try:
            estatus = (Avance_Usuario
                        .select(Avance_Usuario)
                        .where(
                            Avance_Usuario.usuario == id_usuario, 
                            Avance_Usuario.ejercicio == id_ejercicio)
                        .get()
                        ) 

            estatus.intento = estatus.intento + 1
    
            if resultado == True and estatus.resuelto == False:
                estatus.resuelto = True

            actualizacion = estatus.save()

        except:
            avance = Avance_Usuario(
                usuario = id_usuario,
                ejercicio = id_ejercicio,
                resuelto  = resultado,
                intento = 1
                )

            actualizacion = avance.save()


        return actualizacion
