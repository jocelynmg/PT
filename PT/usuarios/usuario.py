from peewee import AutoField, CharField, IntegrityError
from usuarios.model import BaseModel
import hashlib


class Usuario(BaseModel):
    """Define un usuario con username y contraseña"""

    id_usuario = AutoField()
    username = CharField(max_length = 15, unique = True)
    password = CharField(max_length = 64)
  

    def insercionBD(self):
        """Inserta un nuevo usuario en la BD"""

        #CIFRADO DE CONTRASEÑA
        cifrado = hashlib.sha256()
        cifrado.update(str(self.password).encode('utf8'))

        #SE DEFINEN LOS PARAMETROS DEL USUARIO
        usuario = Usuario(
            username = self.username,
            password = cifrado.hexdigest()
            )
        
        #INSERTA EL USUARIO EN LA BASE DE DATOS
        try:
            resultado = usuario.save()

        #CACHA EL ERROR SI EL USUARIO YA EXISTE
        except IntegrityError as err:
            print('Error: {}'.format(err))
            resultado = 0

        return resultado
    
    def identificarseBD(self):
        """Recupera un usuario registrado previamente en la BD"""

        #CIFRA LA CONTRSEÑA
        cifrado = hashlib.sha256()
        cifrado.update(str(self.password).encode('utf8'))

        #SE MANDA EL QUERY Y REGRESA LA TUPLA DEL USUARIO SI EXISTE
        try:
            resultado = (Usuario
                        .select(Usuario)
                        .where(
                            Usuario.username == self.username, 
                            Usuario.password == cifrado.hexdigest())
                        .get()
                        )  

        #CACHA EL ERROR SI LOS DATOS NO SE ENCUENTRAN EN LA BASE
        except:
            resultado = [0, self]

        return resultado
