import subprocess, logoUAM, color
from ejercicios.ejercicio import Ejercicio
from ejercicios.avance.avance_usuario import Avance_Usuario
import ejercicios.levantarDocker
import ejercicios.rmCommand
import ejercicios.rmiCommand
import ejercicios.stopCommand
import ejercicios.miDocker
import ejercicios.miNetwork
import ejercicios.miTimeZone
import ejercicios.renombrarImagen


def inicio():
    """Muestra pantalla de bienvenida a los usuarios para iniciar sesión
    o registrase en la aplicación"""
    
    #SE INSTANCIA UN OBJETO COLOR PARA DAR FORMATO AL TEXTO
    c = color.Color()
    #LIMPIA TERMINAL Y MUESTRA CABECERA
    subprocess.call('clear')
    logo = logoUAM.printLogo()
    print(logo)
    print(c.BOLD + ' ¡Hola, bienvenid@!' + c.END)
    print(' Elige la opción que deseas para ingresar a la aplicación.')
    print("""
        1. Iniciar sesión
        2. Registrarse
        3. Salir
    """)
    opcion = input(c.BOLD +' Tu opción: ' + c.END)

    #REGRESA LA OPCIÓN ELEGIDA POR EL USUARIO
    return opcion


def seleccionTipoEjercicio(usuario):
    """Muestra pantalla donde el usuario elige el tipo de ejercicios que quiere
    resolver, así como el avance"""
    
    #SE INSTANCIA UN OBJETO COLOR PARA DAR FORMATO AL TEXTO
    c = color.Color()
    validacion = True

    while validacion:

        subprocess.call('clear')
        logo = logoUAM.printLogo()
        print(logo)
        #SE LISTAN LOS TIPOS DE EJERCICIOS DISPONIBLES
        print(c.BOLD + f'¡Hola {usuario.username.upper()}!' + c.END + ',')
        print('A continuación puedes elegir el tipo de ejercicio a realizar.')
        print("""
            1. Prácticar comandos de Docker
            2. Troubleshooting en Docker
            3. Retos de comandos en Docker
            4. Salir 
        """)

        opcion = input(c.BOLD+'Tu opción: '+c.END)

        try:
            subprocess.call('clear')

            if opcion == '1':
                validacion = False
                #LANZA LA VISTA PARA PRACTICAR COMANDOS
                seleccionEjercicio(usuario, "practica")
                seleccionTipoEjercicio(usuario)

            elif opcion == '2':
                validacion = False
                #LANZA LA VISTA PARA PRACTICAR TROUBLESHOOTING
                seleccionEjercicio(usuario, "problema")
                seleccionTipoEjercicio(usuario)
            
            elif opcion == '3':
                validacion = False
                #LANZA LA VISTA PARA LOS RETOS DE COMANDOS
                seleccionEjercicio(usuario, "reto")
                seleccionTipoEjercicio(usuario)

            elif opcion == '4':
                #SALE DE LA APLICACIÓN
                print(c.BOLD + c.YELLOW +f'\n¡Hasta luego, {usuario.username.upper()}!\n'+c.END)
                break
            
            else:
                #SE ATRAPA EL ERROR EN CASO DE QUE INTRODUZCAN OTRA OPCIÓN
                raise ValueError('OpcionInvalida')

        except ValueError:
            print('\n¡Opción inválida! :(, intenta otra vez.\n')
            continue


def seleccionEjercicio(usuario, tipo):
    """Muestra los ejercicios disponibles dependiendo el tipo de ejercicio"""

    #SE INSTANCIA UN OBJETO COLOR PARA DAR FORMATO AL TEXTO
    c = color.Color()

    logo = logoUAM.printLogo()
    print(logo)
    avance = Avance_Usuario()
    

    #SE INSTANCIA UN OBJETO EJERCICIO
    listaEjercicios = Ejercicio()
    #SE RECUPERA LA LISTA DE EJERCICIOS EN LA BD DE ACUERDO AL TIPO DE EJERCICIO
    listaEjercicios = listaEjercicios.recuperarEjercicios(tipo)

    print('De acuerdo '+ c.BOLD + f'{usuario.username.upper()}'+c.END+', vamos a realizar'
        + ' algunos ejercicios en el servidor Docker.')
    print('\nElige de la siguiente lista cuál quieres hacer:\n')

    #MUESTRA LA LISTA DE EJERCICIOS
    for ejercicio in enumerate(listaEjercicios, 1):
        listAvance = avance.recuperarAvance(ejercicio[1], usuario)
        print(f"\t{ejercicio[0]}. {ejercicio[1].descripcion}".ljust(40), end=" ")
        
        try:
            resuelto = listAvance.resuelto
            intentos = listAvance.intento
            #print(f"Intentos: {listAvance.intento}\tResuelto: {listAvance.resuelto}".rjust(20))
        except:
            resuelto = 'No'
            intentos = '0'

            #print("Intentos: 0\tResuelto: No".rjust(20))
        if resuelto == True:
            resuelto = 'Sí'
        elif resuelto == False:
            resuelto = 'No'
        
        print(f"Intentos: {intentos}\tResuelto: {resuelto}".rjust(20))
    
    print(f"\t{len(listaEjercicios)+1}. Regresar al menú principal")

    #SE ESPERA LA ELECCIÓN DEL USUARIO
    opcion = int(input(c.BOLD+"\nTu opción: "+c.END))
    
    if opcion >= 1 and opcion <= len(listaEjercicios):
        #SE OBTIENE EL EJERCICIO Y EL NOMBRE
        ejercicio = listaEjercicios[opcion-1]

        llamarEjercicio(ejercicio, usuario)
    else:
        pass

    return True


def llamarEjercicio(ejercicio, usuario):
    """Este módulo se dedica a llamar al script del ejercicio seleccionado"""

    #SE INSTANCIA UN OBJETO COLOR PARA DAR FORMATO AL TEXTO
    c = color.Color()

    #SE INSTANCIA UN OBJETO AVANCE_USUARIO PARA GUARDAR EL AVANCE
    avance = Avance_Usuario()
    #SE OBTIENE EL NOMBRE DEL EJERCICIO
    nombreEjercicio = ejercicio.nombre

    #SE MANDA A LLAMAR AL SCRIPT DEL EJERCICIO
    resultado = eval(f"ejercicios.{nombreEjercicio}.vistaEjercicio(usuario)")

    #SE ACTUALIZAN LAS ESTADÍSTICAS PARA EL USUARIO
    avance.actualizarAvance(ejercicio, usuario, resultado[1])

    #SI EL RESULTADO ESTÁ MAL SE MANDA A LLAMAR EL MODULO DE AYUDA
    if resultado[1] == False:
        mostrarAyuda(ejercicio, usuario)
    else:
        print(c.BOLD + f'\n\n\t¡Bien hecho, tu resultado es '+ c.GREEN +'CORRECTO' + c.END + c.BOLD +'! \n\n'+c.END)
        input(c.BOLD+"Da enter para continuar..."+c.END)


    return resultado


def mostrarAyuda(ejercicio, usuario):
    """Muestra las opciones de ayuda y resultado cuando el resultado es 
    incorrecto"""

    #SE INSTANCIA UN OBJETO COLOR PARA DAR FORMATO AL TEXTO
    c = color.Color()
    
    validacion = True
    logo = logoUAM.printLogo()

    #SE OBTIENE EL NOMBRE DEL EJERCICIO
    nombreEjercicio = ejercicio.nombre

    while validacion:
        #SE MUESTRAN LAS OPCIONES CUANDO EL EJERCICIO ES INCORRECTO
        subprocess.call('clear')
        print(logo)            
        print(c.BOLD +'¡Tu resultado es ' + c.YELLOW + 'INCORRECTO' + c.END + c.BOLD +'!\n'+c.END)
        print("""¿Necesitas ayuda? A continuación puedes elegir entre las siguientes opciones.
    
        1. Mostrar ayuda
        2. Ver respuesta
        3. Intentar de nuevo
        4. Regresar al menú principal
        """)

        opcion = input(c.BOLD+"Tu opción: "+c.END)

        try:
            subprocess.call('clear')

            #SE MUESTRA LA AYUDA PARA EL EJERCICIO
            if opcion == '1':
                validacion = False
                subprocess.call('clear')
                print(logo)            
                print("Aquí tienes una pequeña ayuda:\n")
                print(eval(f"ejercicios.{nombreEjercicio}.ayudaEjercicio()"))
                #SE PREGUNTA SI SE QUIERE INTENTAR NUEVAMENTE
                reintento = input(c.BOLD+"\n¿Quieres intentar de nuevo? [s/n]: "+c.END)
                
                if reintento == 's':
                    llamarEjercicio(ejercicio, usuario)
                elif reintento == 'n':
                    continue
                
                return True

            #SE MUESTRA EL RESULTADO DEL EJERCICIO
            elif opcion == '2':
                validacion = False
                subprocess.call('clear')
                print(logo)
                print(eval(f"ejercicios.{nombreEjercicio}.respuestaEjercicio()"))
                #SE PREGUNTA SI SE QUIERE INTENTAR NUEVAMENTE EL EJERCICIO
                reintento = input(c.BOLD+"\n¿Quieres intentar de nuevo? [s/n]: "+c.END)
                
                if reintento == 's':
                    llamarEjercicio(ejercicio, usuario)
                elif reintento == 'n':
                    continue

                return True

            #SE LLAMA DE NUEVO EL EJERCICIO
            elif opcion == '3':
                validacion = False
                llamarEjercicio(ejercicio, usuario)

            #REGRESA AL MENÚ PRINCIPAL
            elif opcion == '4':
                validacion = False

            else:
                raise ValueError('OpcionInvalida')

        except ValueError:
            print('\n¡Opción inválida! :(, intenta otra vez.\n')
            continue
    

    return True
