import logoUAM
import ejercicios.levantarDocker
from ejercicios.ejercicio import Ejercicio

class Tipos:
    """Define los tipos de ejercicios que puede hacer el usuario"""

    def practicarComandos(self, usuario):
        logo = logoUAM.printLogo()
        print(logo)
        print(f'Ok {usuario.nombre}, vamos a practicar algunos comandos.')
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

        print(f'Ok {usuario.nombre}, vamos a realizar algunos ejercicios de'
                + ' troubleshooting')
        print('\nElige de la siguiente lista cuál quieres hacer:\n')

        #SE INSTANCIA UN OBJETO EJERCICIO
        getEjercicios = Ejercicio()
        #SE RECUPERA LA LISTA DE EJERCICIOS
        getEjercicios = getEjercicios.recuperarEjercicios()

        listEjercicios = [e for e in getEjercicios]
    
        #MUESTRA LA LISTA DE EJERCICIOS
        for ejercicio in enumerate(listEjercicios, 1):
            print(ejercicio[0], ejercicio[1].descripcion)
        

        opcion = int(input("\nTu opción: "))
        #print(opcion)
        #print(listEjercicios[opcion-1].nombre,
        #    listEjercicios[opcion-1].id_ejercicio)

        input()

        nombre = listEjercicios[opcion-1].nombre


        resultado = eval(f"ejercicios.{nombre}.vistaEjercicio(usuario)")
        print(f'Tu resultado es el siguiente {resultado}')



        return True