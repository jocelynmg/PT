import logoUAM, color
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


def limpiarEscenario():
    """Limpia el ejercicio después de que haya acabado el usuario"""

    #SE ELIMINAN TODOS LOS CONTENEDORES
    sp.run('docker rm -f $(docker ps -aq)', capture_output=True, shell=True)

    #SE ELIMINAN TODAS LAS IMAGENES
    sp.run('docker rmi -f $(docker images -q)', capture_output=True, shell=True)

    return True


def ayudaEjercicio():

    ayuda = """
    + Intenta hacer uso de dos comandos, asigna la salida de los IDs al comando
      para eliminar los contenedores.

    + Para ver solo los IDs de los contenedores puedes usar esta bandera:

        -q \t Muestra solamente los IDs
    
    + Puedes utilizar la siguiente bandera con el comando rm.

        -f \t Forza la eliminación de contenedores en ejecución

    """

    return ayuda


def respuestaEjercicio():

    respuesta = """
    + Una forma de resolver el ejercicio es con el siguiente comando:

        docker rm -f $(docker ps -aq)

    """

    return respuesta


def evaluarEjercicio():
    """Función que evalúa el Nivel 2 de retos"""

    #SE EVALÚA LA RESPUESTA DEL USUARIO
    check = sp.run(['docker','ps','-aq'], capture_output=True, encoding='utf-8')
    limpiarEscenario()
    
    return False if len(check.stdout) > 0 else True


def vistaEjercicio(usuario):
    """Función que crea el Nivel 2 de retos"""

    #SE INSTANCIA UN OBJETO COLOR PARA DAR FORMATO AL TEXTO
    c = color.Color()

    #SE LIMPIA LA PANTALLA
    sp.run('clear')   
    logo = logoUAM.printLogo()
    print(logo)

    sentencia = """
    A continuación, intenta realizar lo siguiente:
    
        ELIMINAR TODOS los contenedores con UN sólo comando.
        
    IMPORTANTE: Una vez que aparezca el prompt, solo podrás introducir una línea, 
    por lo que introduce tu respuesta y da enter cuando estés seguro de que ya 
    está correcta. Al dar enter se comenzará con la evaluación del ejercicio.
    
    """

    print(sentencia)

    input(c.BOLD + 'Da enter para comenzar...' + c.END)

    #SE COMIENZA A PREPARAR EL EJERCICIO
    print('\nPreparando tu escenario, espera a que aparezca el prompt.\n')

    prepararEjercicio()

    print('\n')

    #SE CARGAN LOS CONTENDORES
    for i in range(3):
        sp.run(['docker','run','-dit','ubuntu'], capture_output=True)
        sp.run(['docker','run','-d','ubuntu'], capture_output=True)
    
    #SE MUESTRAN LOS CONTENDEORES 
    sp.run(['docker','ps','-a'], capture_output=False, encoding='utf-8')
    
    cmd = input(c.BOLD +'\n\nTuPrompt$ ' + c.END)
    #SE INTRODUCE EL COMANDO DEL USUARIO
    sp.run(cmd, capture_output=False, encoding='utf-8', shell=True)

    #SE MANDA A EVALUAR EL EJERCICIO
    resultado = evaluarEjercicio()

    resultadoEjercicio = [usuario, resultado]
    sleep(2)

    return resultadoEjercicio