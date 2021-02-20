import logoUAM
import subprocess
import usuarios.usuario as user
from getpass import getpass

class Acciones:
    """Define los métodos utilizados por los usuarios"""

    def registrarse(self):
        """Método para registro de nuevos usuarios en la aplicación"""
        
        #VALIDA QUE EL USUARIO NO EXISTA YA EN LA BASE DE DATOS
        validacion = True
        #SE INCREMENTA CUANDO FALLA EL REGISTRO DE UN NUEVO USUARIO
        intento = 0

        #SE EJECUTARÁ EL WHILE SIEMPRE QUE SE INGRESE UN USUARIO EXISTENTE
        while validacion:

            subprocess.call('clear')
            logo = logoUAM.printLogo()
            print(logo)
            print(' REGISTRO.')
            #PIDE LOS DATOS DE NUEVO USUARIO
            if intento == 0 :
                print(' A continuación se te solicitará Nombre, Username y Password' 
                +' para completar tu registro:\n')
            #MUESTRA QUE EL USUARIO YA ESTA EN LA BASE DE DATOS
            else:
                print(' ¡El usuario ingresado ya existe!, intenta con otro.\n')

            nombre = input('  Nombre: ')
            username = input('  Usuario: ')
            password = getpass(prompt = '  Password: ')

            #SE CREA UNA INSTANCIA DE USUARIO
            usuario = user.Usuario(
                nombre = nombre,
                username = username,
                password = password
                )

            #LLAMA AL METODO USUARIO PARA INSERTARLO EN LA BASE DE DATOS
            registro = usuario.insercionBD()

            if registro >= 1:
                validacion = False
                return usuario

            else:
                intento = intento + 1


    def iniciarSesion(self):
        """Método para el inicio de sesión de los usuarios"""

        validacion = True
        intento = 0

        while validacion:
        
            subprocess.call('clear')
            logo = logoUAM.printLogo()
            print(logo)
            print(' INICIO DE SESIÓN.')
            if intento == 0:
                print(' Ingresa tu usuario y password para accesar:\n')
            else:
                print(' Datos incorrectos, verifica el usuario y/o contraseña.\n')

            try:
                username = input('  Usuario: ')
                password = getpass(prompt = '  Password: ')

                usuario = user.Usuario(
                    nombre = '',
                    username = username,
                    password = password
                    )

                login = usuario.identificarseBD()

                #Valida que los datos del usuario coninciden en la BD
                if username == login.username:
                    print(login.username)
                    print(f'\n¡Bienvenid@ {login.nombre}!, {login.username}')
                    print(f'\n¡Haz iniciado sesión como {username} y contraseña'
                                + f' {password}!\n')
                    validacion = False
                
                    return login

            #Regresa un dato None cuando los datos no hacen match en la BD
            except AttributeError:
                print(' Datos incorrectos, inténtalo de nuevo')
                intento = intento + 1
