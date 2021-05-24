import sys, logoUAM, color
import subprocess
from time import sleep

def prepararEjercicio():
    """Este método prepara el escenario para el ejercicio"""

    #SE ELIMINAN TODOS LOS CONTENEDORES
    subprocess.run('docker rm -f $(docker ps -aq)', capture_output=True, shell=True)

    #SE ELIMINAN TODAS LAS IMAGENES
    subprocess.run('docker rmi -f $(docker images -q)', capture_output=True, shell=True)

    #SE CARGA LA IMAGEN QUE SE VA A UTILIZAR
    subprocess.run(['docker','load','-i','util/images/python.tar'],\
                                    capture_output=False)
    
    #SE APAGA EL SERVICIO DE DOCKER
    subprocess.run(
        'sudo systemctl stop docker.service'.split(),
        stdout = subprocess.DEVNULL,
        stderr = subprocess.DEVNULL
        )


    return True


def limpiarEscenario():

    #SE ELIMINAN TODOS LOS CONTENEDORES
    subprocess.run('docker rm -f $(docker ps -aq)', capture_output=True, shell=True)

    #SE ELIMINAN TODAS LAS IMAGENES
    subprocess.run('docker rmi -f $(docker images -q)', capture_output=True, shell=True)

    #SE ENCIENDE DE NUEVO EL SERVICIO DOCKER
    subprocess.run(
        'sudo systemctl start docker.service'.split(),
        stdout = subprocess.DEVNULL,
        stderr = subprocess.DEVNULL
        )

    return True

def evaluarEjercicio():
    resultado = False

    #SE SACA LA LISTA DE LOS DOCKER QUE HAYA EJECUTADO EL USUARIO
    proceso = subprocess.Popen(
        'docker ps -a'.split(),
        stdout = subprocess.PIPE,
        stderr = subprocess.DEVNULL
        )

    proceso.wait()
    salida = proceso.stdout.read()
    proceso.stdout.close()
    salida = salida.decode(sys.getdefaultencoding()).split('\n')

    #EVALUA QUE SE TENGAN LOS PARÁMETROS SOLICITADOS EN EL DOCKER
    for line in salida:

        if 'python:3.6-slim-stretch' in line and '\"sleep 5\"' in line and 'PythonTest' in line:
            resultado = True


    return resultado


def ayudaEjercicio():

    ayuda = """
    + Intenta revisar el estado del demonio de Docker.

        systemctl status docker.service        --> Valida el estado de Docker
    
    + Recuerda que en Docker puedes utilizar los siguientes comandos:

        -d \t modo Detach
    
    + Al nombrar el contenedor, toma en cuenta mayúsculas y minúsculas.
    
    """

    return ayuda


def respuestaEjercicio():

    respuesta = """
    + Intenta con la siguiente secuencia de comandos para resolver el ejercicio:

        systemctl status docker.service        --> Valida el estado de Docker
        sudo systemctl start docker.service    --> Levanta el servicio Docker
        docker run -d --name=PythonTest python:3.6-slim-stretch sleep 5
    
    """

    return respuesta


def vistaEjercicio(usuario):

    #SE INSTANCIA UN OBJETO COLOR PARA DAR FORMATO AL TEXTO
    c = color.Color()

    subprocess.run('clear')

    logo = logoUAM.printLogo()
    print(logo)
    sentencia = """
    Uamito tiene que levantar un contenedor usando la imagen de python con el
    tag 3.6-slim-stretch, con el nombre "PythonTest", en modo DETACH y que ejecute
    el comando "sleep 5", pero tiene problemas para lograrlo. Ayuda a Uamito a 
    levantar su Docker.

    Una vez que el contenedor con las características mencionadas se haya 
    ejecutado, se dará como bueno el ejercicio.

    Escribe 'exit' cuando hayas finalizado o en cualquier otro momento para 
    regresar a la aplicación principal.
    """
    print(sentencia)

    input(c.BOLD + 'Da enter para comenzar...' + c.END)
    
    #SE COMIENZA A PREPARAR EL EJERCICIO
    print('\nPreparando tu escenario, espera a que aparezca el prompt.\n')

    #SE LLAMA A LA FUNCIÓN PARA PREPARAR EL EJERCICIO
    prepararEjercicio()
    
    #ENTRANDO A KORN SHELL
    print(c.YELLOW + c.BOLD +'\nAhora estás en KornShell' + c.END)
    subprocess.call('ksh')

    #UNA VEZ QUE EL USUARIO ENTRA EXIT EN LA TERMINAL, SE EVALUA EL EJERCICIO
    print(c.CYAN + c.BOLD + '\nEvaluando el ejercicio...' + c.END)
    resultado = evaluarEjercicio()

    limpiarEscenario()
    
    resultadoEjercicio = [usuario, resultado]
    sleep(2)

    return resultadoEjercicio