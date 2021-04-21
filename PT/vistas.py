import subprocess, logoUAM
import ejercicios.levantarDocker
from ejercicios.ejercicio import Ejercicio
from ejercicios.avance.avance_usuario import Avance_Usuario

def inicio():
    """Muestra pantalla de bienvenida a los usuarios para iniciar sesión
        o registrase en la aplicación
        """
    #LIMPIA TERMINAL Y MUESTRA CABECERA
    subprocess.call('clear')
    logo = logoUAM.printLogo()
    print(logo)
    print(' ¡Hola, bienvenid@!')
    print(' Elige la opción que deseas para ingresar a la aplicación:')
    print("""
        1. Iniciar sesión
        2. Registrarse
        3. Salir
    """)
    opcion = input(' Tu opción: ')

    #REGRESA LA OPCIÓN ELEGIDA POR EL USUARIO
    return opcion


def seleccionTipoEjercicio(usuario):
    """Muestra pantalla donde el usuario elige el tipo de ejercicos que quiere
    resolver, así como el avance"""
    
    validacion = True

    while validacion:

        subprocess.call('clear')
        logo = logoUAM.printLogo()
        print(logo)
        #SE LISTAN LOS TIPOS DE EJERCICIOS DISPONIBLES
        print(f'¡Hola {usuario.username.upper()}!,')
        print('A continuación puedes elegir el tipo de ejercicio a realizar')
        print("""
            1. Retos para prácticar comandos de Docker
            2. Troubleshooting en Docker
            3. Ver mis estádisticas
            4. Salir 
        """)

        opcion = input('Tu opción: ')

        try:
            subprocess.call('clear')

            if opcion == '1':
                validacion = False
                #LANZA LA VISTA PARA PRACTICAR COMANDOS
                practicarComandos(usuario)
                seleccionTipoEjercicio(usuario)

            elif opcion == '2':
                validacion = False
                #LANZA LA VISTA PARA PRACTICAR TROUBLESHOOTING
                troubleshootingDocker(usuario)
                seleccionTipoEjercicio(usuario)

            elif opcion == '3':
                validacion = False
                #LANZA LA VISTA PARA MOSTRAR LAS ESTADISTÍCAS
                print(f'¡Vamos a ver tus estádisticas {usuario.username}!')
                seleccionTipoEjercicio(usuario)

            elif opcion == '4':
                #SALE DE LA APLICACIÓN
                print(f'¡Hasta luego, {usuario.username.upper()}!')
                break
            
            else:
                #SE ATRAPA EL ERROR EN CASO DE QUE INTRODUZCAN OTRA OPCIÓN
                raise ValueError('OpcionInvalida')

        except ValueError:
            print('\n¡Opción inválida! :(, intenta otra vez\n')
            continue


def practicarComandos(usuario):
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


def troubleshootingDocker(usuario):
    logo = logoUAM.printLogo()
    print(logo)

    #SE INSTANCIA UN OBJETO EJERCICIO
    listaEjercicios = Ejercicio()
    #SE RECUPERA LA LISTA DE EJERCICIOS EN LA BD
    listaEjercicios = listaEjercicios.recuperarEjercicios("problema")

    print(f'De acuerdo {usuario.username.upper()}, vamos a realizar'
        + ' algunos ejercicios de troubleshooting.')
    print('\nElige de la siguiente lista cuál quieres hacer:\n')

    #MUESTRA LA LISTA DE EJERCICIOS DE TIPO PROBLEMA
    for ejercicio in enumerate(listaEjercicios, 1):
        print(ejercicio[0], ejercicio[1].descripcion)

    #SE ESPERA LA ELECCIÓN DEL USUARIO
    opcion = int(input("\nTu opción: "))
    
    if opcion >= 1 and opcion <= len(listaEjercicios):
        #SE OBTIENE EL EJERCICIO Y EL NOMBRE DEL PROBLEMA
        ejercicio = listaEjercicios[opcion-1]

        llamarEjercicio(ejercicio, usuario)

    return True


def llamarEjercicio(ejercicio, usuario):

    #SE INSTANCIA UN OBJETO AVANCE_USUARIO PARA GUARDAR EL AVANCE
    avance = Avance_Usuario()
    #SE OBTIENE EL NOMBRE DEL EJERCICIO
    nombreEjercicio = ejercicio.nombre

    #SE MANDA A LLAMAR AL SCRIPT DEL EJERCICIO
    resultado = eval(f"ejercicios.{nombreEjercicio}.vistaEjercicio(usuario)")

    #SE ACTUALIZAN LAS ESTADÍSTICAS PARA EL USUARIO
    actualizacion = avance.actualizarAvance(ejercicio, usuario, resultado[1])

    if actualizacion >= 1:
        print('Avance actualizado')

    #SI EL RESULTADO ESTÁ MAL SE MANDA A LLAMAR EL MODULO DE AYUDA
    if resultado[1] == False:
        mostrarAyuda(ejercicio, usuario)
    else:
        print(f'Tu resultado es CORRECTO, ¡Bien hecho!\n')
        input("Da enter para continuar")


    return resultado


def mostrarAyuda(ejercicio, usuario):
    
    validacion = True
    logo = logoUAM.printLogo()
    nombreEjercicio = ejercicio.nombre

    while validacion:

        subprocess.call('clear')
        print(logo)            
        print(f'¡Tu resultado es INCORRECTO!\n')
        print("¿Necesitas ayuda? A continuación puedes elegir entre las "
            + "siguientes opciones:")
        print("""
            1. Mostrar ayuda.
            2. Ver respuesta.
            3. Intentar de nuevo.
            4. Yo puedo sol@. Regresar la lista de ejercicios.
            """)

        opcion = input("Tu opción: ")

        try:
            subprocess.call('clear')

            if opcion == '1':
                validacion = False
                subprocess.call('clear')
                print(logo)            
                print("Aquí tienes una pequeña ayuda:\n")
                print(eval(f"ejercicios.{nombreEjercicio}.ayudaEjercicio()"))
                reintento = input("\n¿Quieres intentar de nuevo? [si/no]: ")
                
                if reintento == 'si':
                    llamarEjercicio(ejercicio, usuario)
                elif reintento == 'no':
                    continue
                
                return True


            elif opcion == '2':
                validacion = False
                subprocess.call('clear')
                print(logo)
                print(eval(f"ejercicios.{nombreEjercicio}.respuestaEjercicio()"))
                reintento = input("\n¿Quieres intentar de nuevo? [si/no]: ")
                
                if reintento == 'si':
                    llamarEjercicio(ejercicio, usuario)
                elif reintento == 'no':
                    continue

                return True

            elif opcion == '4':
                validacion = False

            else:
                raise ValueError('OpcionInvalida')

        except ValueError:
            print('\n¡Opción inválida! :(, intenta otra vez\n')
            continue
    

    return True
