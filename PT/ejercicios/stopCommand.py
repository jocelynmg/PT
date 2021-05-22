import logoUAM
from time import sleep
import subprocess as sp

def prepararEjercicio():
    """Funcion que limpia el escenario al inicio y al final de los ejercicios"""
    
    #SE ELIMINAN TODOS LOS CONTENEDORES
    sp.run('docker rm -f $(docker ps -aq)', capture_output=True, shell=True)
    
    #SE ELIMINAN TODAS LAS IMAGENES
    sp.run('docker rmi -f $(docker images -q)', capture_output=True, shell=True)

    #SE CARGA LA IMAGEN QUE SE VA A UTILIZAR
    sp.run(['docker','load','-i','util/images/ubuntu.tar'],\
                                                    capture_output=False)

    return True


def limpiarEscenario():
    """Limpia el ejercicio después de que haya acabado el usuario"""

    #SE ELIMINAN TODOS LOS CONTENEDORES
    sp.run('docker rm -f $(docker ps -aq)', capture_output=True, shell=True)

    #SE ELIMINAN TODAS LAS IMAGENES
    sp.run('docker rmi -f $(docker images -q)', capture_output=True, shell=True)

    return True


def ayudaEjercicio():
    #SE PROPORCIONA AYUDA AL USUARIO
    ayuda = """
    + Intenta hacer uso de dos comandos, asigna la salida de los IDs al comando
      para detener los dockers.

    + Para ver solo los IDs de los contenedores puedes usar esta bandera:

        -q \t Muestra solamente los IDs
    
    """

    return ayuda


def respuestaEjercicio():
    #SE DA LA RESPUESTA DEL EJERCICIO AL USUARIO
    respuesta = """
    + Una forma de resolver el ejercicio es con el siguiente comando:
        
        docker stop $(docker ps -aq)

    """
    
    return respuesta


def evaluarEjercicio():
    """Función que evalúa el ejercicio Nivel 1"""

    #SE EVALUA SI SE DETUVIERON TODOS LOS CONTENEDORES
    check = sp.run(['docker','ps','-q'], capture_output=True, encoding='utf-8')
    limpiarEscenario()

    return False if len(check.stdout) > 0 else True


def vistaEjercicio(usuario):
    """Función creadora del escenario nivel 1"""

    #SE LIMPIA LA PANTALLA
    sp.run('clear')
    logo = logoUAM.printLogo()
    print(logo)

    sentencia = """
    A continuación, intenta realizar lo siguiente:
    
        DETENER TODOS los contenedores con UN sólo comando. 
    
    IMPORTANTE: Una vez que aparezca el prompt, solo podrás introducir una línea, 
    por lo que introduce tu respuesta y da enter cuando estés seguro de que ya 
    está correcta. Al dar enter se comenzará con la evalucación del ejercicio.
    """
    print(sentencia)

    input('Da enter para comenzar...')
    #SE COMIENZA A PREPARAR EL EJERCICIO
    print('\nPreparando tu escenario, espera a que aparezca el prompt.\n')

    prepararEjercicio()

    print('\n')

    #SE CARGAN LOS CONTENEDORES PARA ELEJERCICIO
    for i in range(7):
        sp.run(['docker','run','-dit','ubuntu'], capture_output=True)
    
    #SE MUESTRAN los contenedores activos
    sp.run(['docker','ps'], capture_output=False, encoding='utf-8')
    
    cmd = input('\n\nTuPrompt$ ')
    #SE EJECUTA EL COMANDO INTRODUCIDO POR EL USUARIO
    sp.run(cmd, capture_output=False, encoding='utf-8', shell=True)

    #SE MANDA A EVALUAR EL EJERCICIO
    resultado = evaluarEjercicio()

    resultadoEjercicio = [usuario, resultado]
    sleep(2)

    return resultadoEjercicio
