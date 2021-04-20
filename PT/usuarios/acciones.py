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

        #SE EJECUTARÁ EL WHILE SIEMPRE QUE SE INGRESE UN USUARIO YA EXISTENTE
        while validacion:

            subprocess.call('clear')
            logo = logoUAM.printLogo()
            print(logo)
            print(' REGISTRO.')
            #PIDE LOS DATOS DE NUEVO USUARIO
            if intento == 0 :
                print(' A continuación se te solicitará Username y Password' 
                +' para completar tu registro:\n')
            #MUESTRA QUE EL USUARIO YA ESTA EN LA BASE DE DATOS
            else:
                print(' ¡El usuario ingresado ya existe!, intenta con otro.\n')

            username = input('  Usuario: ')
            password = getpass(prompt = '  Password: ')

            #SE CREA UNA INSTANCIA DE USUARIO
            usuario = user.Usuario(
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

        #VALIDA EL INGRESO DE DATOS CORRECTOS POR EL USUARIO
        validacion = True
        #SE INCREMENTA CUANDO EL USUARIO INGRASA UN DATO ERRÓNEO
        intento = 0

        while validacion:
        
            subprocess.call('clear')
            logo = logoUAM.printLogo()
            print(logo)
            print(' INICIO DE SESIÓN.')
            #PIDEO LOS DATOS DE INICIO DE SESIÓN
            if intento == 0:
                print(' Ingresa tu usuario y password para accesar:\n')
            #MUESTRA QUE LOS DATOS INGRESADOS ESTÁN MAL
            else:
                print(' Datos incorrectos, verifica el usuario y/o contraseña.\n')

            try:
                username = input('  Usuario: ')
                password = getpass(prompt = '  Password: ')

                usuario = user.Usuario(
                    username = username,
                    password = password
                    )

                login = usuario.identificarseBD()

                #VALIDA QUE LOS DATOS DEL USUARIO HACEN MATCH EN LA BD
                if username == login.username:
                    print(login.username)
                    print(f'\n¡Bienvenid@ {login.username}!')
                    print(f'\n¡Haz iniciado sesión como {username} y contraseña'
                                + f' {password}!\n')
                    validacion = False
                
                    return login

            #REGRESA UN DATO NONE CUANDO LOS DATOS NO HACEN MATCH EN LA BD
            except AttributeError:
                print(' Datos incorrectos, inténtalo de nuevo')
                intento = intento + 1
