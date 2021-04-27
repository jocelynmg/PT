import logoUAM
from time import sleep
import subprocess as sp

def prepararEjercicio():
    """Funcion que limpia el escenario al inicio y al final de los ejercicios"""

    #SE ELIMINAN TODOS LOS CONTENEDORES
    sp.run('docker rm -f $(docker ps -aq)', capture_output=True, shell=True)
    #SE ELIMINAN TODAS LAS IMAGENES
    sp.run('docker rmi -f $(docker images -q)', capture_output=True, shell=True)


def ayudaEjercicio():

    ayuda = "Aquí se pondrá la ayuda el ejercicio\n\n"

    return ayuda


def respuestaEjercicio():

    respuesta = """
    Una forma de resolver el ejercicio es con el siguiente comando:

        docker rm -f $(docker ps -aq)

    """

    return respuesta


def evaluarEjercicio():
    """Función que evalúa el Nivel 2"""

    #SE EVALÚA LA RESPUESTA DEL USUARIO
    check = sp.run(['docker','ps','-aq'], capture_output=True, encoding='utf-8')
    prepararEjercicio()
    
    return False if len(check.stdout) > 0 else True


def vistaEjercicio(usuario):
    """Función que crea el Nivel 2"""

    #SE LIMPIA LA PANTALLA
    sp.run('clear')
    prepararEjercicio()
    
    #SE CARGA LA IMAGEN QUE SE VA A UTILIZAR
    sp.run(['docker','load','-i','/home/pete/Escritorio/ProyectoTerminal/PT/util/images/ubuntu.tar'],\
                                                    capture_output=True)

    logo = logoUAM.printLogo()
    print(logo)
    sentencia = """
    A continuación, intenta realizar lo siguiente:
    
        ELIMINAR TODOS los contenedores con UN sólo comando.
        
    Una vez que aparezca el prompt, solo podrás introducir una línea, por lo
    que introduce tu respuesta y da enter cuando estés seguro de que ya está
    correcta. Cuando introduzcas tu respuesta, al dar enter se comenzará con
    la evalucación del ejercicio.
    """

    print(sentencia)

    input('Da enter para comenzar...')
    #SE COMIENZA A PREPARAR EL EJERCICIO
    print('\n\nPreparando tu escenario, espera a que aparezca el prompt...')

    #SE CARGAN LOS CONTENDORES
    for i in range(3):
        sp.run(['docker','run','-dit','ubuntu'], capture_output=True)
        sp.run(['docker','run','-d','ubuntu'], capture_output=True)
    
    #SE MUESTRAN LOS CONTENDEORES 
    sp.run(['docker','ps','-a'], capture_output=False, encoding='utf-8')
    
    cmd = input('\nTuPrompt$')
    #SE INTRODUCE EL COMANDO DEL USUARIO
    sp.run(cmd, capture_output=False, encoding='utf-8', shell=True)

    #SE MANDA A EVALUAR EL EJERCICIO
    resultado = evaluarEjercicio()

    resultadoEjercicio = [usuario, resultado]
    sleep(2)

    return resultadoEjercicio