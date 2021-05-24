import subprocess
import vistas, color
from usuarios import acciones

"""
Este es el módulo principal del Proyecto de Integración para mejorar hábilidades
en el uso de contenedores con tecnología de Docker.
"""

if __name__ == "__main__":

    c = color.Color()
    validacion = True

    while validacion:
        opcion = vistas.inicio()

        try:
            #SE INSTANCIA UN OBJETO ACCIONES
            accion = acciones.Acciones()
            subprocess.call('clear')

            if opcion == '1':
                validacion = False
                #INICIO DE SESIÓN Y ENTRADA A LA APLICACIÓN
                user = accion.iniciarSesion()
                vistas.seleccionTipoEjercicio(user)

            elif opcion == '2':
                validacion = False
                #REGISTRO, INICIO DE SESIÓN Y ENTRADA A LA APPLICACIÓN
                user = accion.registrarse()
                user = accion.iniciarSesion()
                vistas.seleccionTipoEjercicio(user)
            
            elif opcion == '3':
                #SALE DE LA APLICACIÓN
                validacion = False
                print(c.BOLD+c.YELLOW+'\n¡Hasta Luego!\n'+c.END)

            else:
                raise ValueError('OpcionInvalida')

        except ValueError as err:
            print('\n¡Opción inválida! :(, intenta otra vez\n')
            continue
