import logoUAM
import ejercicios.levantarDocker
from ejercicios.ejercicio import Ejercicio
from ejercicios.avance.avance_usuario import Avance_Usuario

class Tipos:
    """Define los tipos de ejercicios que puede hacer el usuario"""

    def practicarComandos(self, usuario):
        logo = logoUAM.printLogo()
        print(logo)
        print(f'Ok {usuario.username.upper()}, vamos a practicar algunos comandos.')
        print('\nElige de la siguiente lista cuál quieres practicar:')

        print("""
        1. Prácticar comando <run>.
        2. Prácticar comando <rm>.
        3. Prácticar más comandos.
        4. Regresar.
        """)

        opcion = input("Tu opción: ")
        opcion = opcion

        return True

    def troubleshootingDocker(self, usuario):
        logo = logoUAM.printLogo()
        print(logo)

        #SE INSTANCIA UN OBJETO EJERCICIO
        listEjercicios = Ejercicio()
        #SE RECUPERA LA LISTA DE EJERCICIOS EN LA BD
        listEjercicios = listEjercicios.recuperarEjercicios("problema")
    
        print(f'De acuerdo {usuario.username.upper()}, vamos a realizar'
            + ' algunos ejercicios de troubleshooting.')
        print('\nElige de la siguiente lista cuál quieres hacer:\n')

        #MUESTRA LA LISTA DE PROBLEMAS
        for ejercicio in enumerate(listEjercicios, 1):
            print(ejercicio[0], ejercicio[1].descripcion)

        opcion = int(input("\nTu opción: "))

        #SE INSTANCIA UN OBJETO AVANCE_USUARIO
        avance = Avance_Usuario()
        
        if opcion >= 1 and opcion <= len(listEjercicios):
            #SE OBTIENE EL EJERCICIO Y EL NOMBRE DEL PROBLEMA
            ejercicio = listEjercicios[opcion-1]
            nombre = ejercicio.nombre

            #SE MANDA A LLAMAR AL SCRIPT DEL EJERCICIO
            resultado = eval(f"ejercicios.{nombre}.vistaEjercicio(usuario)")

            print(f'Tu resultado es el siguiente {resultado}')

            #SE ACTUALIZAN LAS ESTADÍSTICAS PARA EL USUARIO
            actualizacion = avance.actualizarAvance(ejercicio, usuario, resultado[1])

            if actualizacion >= 1:
                print('Avance actualizado')


        return True