import json
import sys, logoUAM, color
import subprocess as sp
from time import sleep

def prepararEjercicio():

    #SE ELIMINAN TODOS LOS CONTENEDORES
    sp.run('docker rm -f $(docker ps -aq)', capture_output=True, shell=True)

    #SE ELIMINAN TODAS LAS IMAGENES
    sp.run('docker rmi -f $(docker images -q)', capture_output=True, shell=True)

    #SE CARGA LA IMAGEN QUE SE VA A UTILIZAR
    sp.run(['docker','load','-i','util/images/base.tar'],\
                                            capture_output=False)
    
    #SE EJECUTA EL DOCKERFILE
    sp.run(['docker', 'build', '-f', 'util/dockerfile', '.'],\
                                            capture_output=True)

    #SE ELIMINA LA IMAGEN BASE QUE SE CREÓ
    sp.run(['docker', 'rmi', 'base'], capture_output=True)
    
    return True


def limpiarEscenario():

    #SE ELIMINAN TODOS LOS CONTENEDORES
    sp.run('docker rm -f $(docker ps -aq)', capture_output=True, shell=True)

    #SE ELIMINAN TODAS LAS IMAGENES
    sp.run('docker rmi -f $(docker images -q)', capture_output=True, shell=True)

    #SE BORRAN TODAS LAS REDES PERSONALIZADAS
    sp.run('docker network rm $(docker network ls -q)', capture_output=True, shell=True)

    return True


def evaluarEjercicio():
    resultado = False
    validaImagen = False
    validaCaracteristicas = False
    cmd = False

    #SE ENVÍA EL COMANDO PARA EVALUAR LA IMAGEN UTILIZADA EN EL CONTENEDOR
    listImagen = ['docker', 'ps', '--filter', 'name=MiTortuga',\
                            '--filter', 'ancestor=myturtle', '-aq']
    testImagen = sp.run(listImagen, capture_output=True, encoding='utf-8')
    
    if len(testImagen.stdout) > 0:
        validaImagen = True

    #SE ENVÍA EL COMANDO PARA EL INSPECT DEL CONTENEDOR
    output = sp.run(['docker','inspect', 'MiTortuga'], capture_output=True,\
                                                            encoding='utf-8')    

    #SE EVALUA QUE SE HAYA COLOCADO CORRECTAMENTE EL NOMBRE DEL CONTENEDOR
    if output.stdout == '[]\n':
        return False

    else:
        #SE OBTIENE UN DICCIONARIO DEL COMANDO DOCKER INSPECT
        inspect = json.loads(output.stdout)[0]
        
        #SE EVALUA NAME, HOSTNAME, RESTART POLICY, TIME_ZONE
        n = inspect.get('Name')
        listcmd = inspect.get('Config').get('Cmd')

        texto = "/usr/games/cowsay -f /usr/share/cowsay/cows/turtle.cow"

        for i in listcmd:
            if texto in i:
                cmd = True

        #SE EVALUA LA OPCIÓN DE DETACH
        ain = inspect.get('Config').get('AttachStdin')
        aout = inspect.get('Config').get('AttachStdout')
        
        if n == '/MiTortuga' and ain == False and aout == True and cmd == True:
            validaCaracteristicas = True

        
    if validaCaracteristicas == True and validaImagen == True:
        resultado = True

    return resultado


def ayudaEjercicio():

    ayuda = """
    + Revisa las imagenes, puedes renombrar las que están cargadas en Docker con
      el siguiente comando.
    
        tag \t Para renombrar una imagen
    
    + Al nombrar el contenedor y la red, toma en cuenta mayúsculas y minúsculas.

    """

    return ayuda


def respuestaEjercicio():

    respuesta = """
    + La siguiente secuencia de comandos da solución al ejercicio: 

        docker tag [ID de la imagen <none>] myturtle
        docker run --name=MiTortuga myturtle
    """

    return respuesta


def vistaEjercicio(usuario):

    #SE INSTANCIA UN OBJETO COLOR PARA DAR FORMATO AL TEXTO
    c = color.Color()

    sp.run('clear')

    logo = logoUAM.printLogo()
    print(logo)
    sentencia = """
    Uamito tienen problemas para levantar su contenedor. El contenedor debe 
    utilizar la imagen myturtle y debe llamarse "MiTortuga", SIN utilizar
    el modo DETACH. Ayuda a Uamito a levantar su contendor.

    Escribe 'exit' cuando hayas finalizado o en cualquier otro momento para 
    regresar a la aplicación principal.
    """
    print(sentencia)

    input(c.BOLD + 'Da enter para comenzar...' + c.END)
    
    print('\nPreparando tu escenario, espera a que aparezca el prompt.\n')

    #SE LLAMA A LA FUNCIÓN PARA PREPARAR EL EJERCICIO
    prepararEjercicio()
    
    #ENTRANDO A KORN SHELL
    print(c.YELLOW + c.BOLD +'\nAhora estás en KornShell' + c.END)
    sp.call('ksh')

    #UNA VEZ QUE EL USUARIO ENTRA EXIT EN LA TERMINAL, SE EVALUA EL EJERCICIO
    print(c.CYAN + c.BOLD + '\nEvaluando el ejercicio...' + c.END)

    resultado = evaluarEjercicio()

    resultadoEjercicio = [usuario, resultado]
    sleep(2)

    return resultadoEjercicio