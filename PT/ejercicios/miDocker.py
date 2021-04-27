import json
import sys, logoUAM
import subprocess as sp
from time import sleep

def prepararEjercicio():

    #SE ELIMINAN TODOS LOS CONTENEDORES
    sp.run('docker rm -f $(docker ps -aq)', capture_output=True, shell=True)

    #SE ELIMINAN TODAS LAS IMAGENES
    sp.run('docker rmi -f $(docker images -q)', capture_output=True, shell=True)

    #SE CARGA LA IMAGEN QUE SE VA A UTILIZAR
    sp.run(['docker','load','-i','/home/pete/Escritorio/ProyectoTerminal/PT/util/images/ubuntu.tar'],\
                                    capture_output=False)
    
    return True


def evaluarEjercicio():
    resultado = False
    validaImagen = False
    validaCaracteristicas = False
    hp = '0'

    #SE ENVÍA EL COMANDO PARA EVALUAR LA IMAGEN UTILIZADA EN EL CONTENEDOR
    listImagen = ['docker', 'ps', '--filter', 'name=MiDocker',\
                            '--filter', 'ancestor=ubuntu', '-aq']
    testImagen = sp.run(listImagen, capture_output=True, encoding='utf-8')
    
    if len(testImagen.stdout) > 0:
        validaImagen = True

    #SE ENVÍA EL COMANDO PARA EL INSPECT DEL CONTENEDOR
    output = sp.run(['docker','inspect', 'MiDocker'], capture_output=True,\
                                                            encoding='utf-8')    

    #SE EVALUA QUE SE HAYA COLOCADO CORRECTAMENTE EL NOMBRE DEL CONTENEDOR
    if output.stdout == '[]\n':
        print(output.stdout)
        return False

    else:
        #SE OBTIENE UN DICCIONARIO DEL COMANDO DOCKER INSPECT
        inspect = json.loads(output.stdout)[0]
        #NAME, HOSTPORT, ATTACH STDIN, STDOUT, STDERR
        n = inspect.get('Name')
        
        #SE EVALUA TANTO EL EXPOSED PORT COMO EL HOST PORT
        try:
            hp = inspect.get('NetworkSettings').get('Ports')\
                                .get('5000/tcp')[0].get('HostPort')

        except TypeError as err:
            err = 'Error: {}'.format(err)
        
        #SE EVALUA LA OPCIÓN DE DETACH
        ain = inspect.get('Config').get('AttachStdin')
        aout = inspect.get('Config').get('AttachStdout')

        if n == '/MiDocker' and hp == '80' and ain == False and aout == False:
            validaCaracteristicas = True
        
    if validaCaracteristicas == True and validaImagen == True:
        resultado = True

    return resultado


def ayudaEjercicio():

    ayuda = "Intenta revisar el estado del demonio de Docker\n\n"

    return ayuda


def respuestaEjercicio():

    respuesta = "Intenta con la siguiente secuencia de comandos: \n\n" \
        + "       systemctl status docker.service \n" \
        + "       sudo systemctl start docker.service \n" \
        + "       docker run -d --name=PythonTest python sleep 5 \n\n"

    return respuesta


def vistaEjercicio(usuario):
    sp.run('clear')

    logo = logoUAM.printLogo()
    print(logo)
    sentencia = """
    Levanta un contenedor de Ubuntu llamado "MiDocker" en modo DETACH y con la
    terminal interactiva, así mismo, debes mapear el puerto 80 del Host hacia
    el puerto 5000 del contenedor.

    Escribe 'exit' cuando hayas finalizado o en cualquier otro momento para 
    regresar a la aplicación principal.
    """
    print(sentencia)

    input('Da enter para cargar tu escenario...\n')

    #SE LLAMA A LA FUNCIÓN PARA PREPARAR EL EJERCICIO
    prepararEjercicio()
    
    #ENTRANDO A KORN SHELL
    print('\nAhora estás en KornShell')
    sp.call('ksh')

    #UNA VEZ QUE EL USUARIO ENTRA EXIT EN LA TERMINAL, SE EVALUA EL EJERCICIO
    print('\nEvaluando ejercicio...')
    sleep(1)
    resultado = evaluarEjercicio()

    resultadoEjercicio = [usuario, resultado]
    sleep(2)

    return resultadoEjercicio