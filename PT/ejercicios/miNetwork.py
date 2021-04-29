import json
import sys, logoUAM
import subprocess as sp
from time import sleep

def prepararEjercicio():

    #SE ELIMINAN TODOS LOS CONTENEDORES
    sp.run('docker rm -f $(docker ps -aq)', capture_output=True, shell=True)

    #SE ELIMINAN TODAS LAS IMAGENES
    sp.run('docker rmi -f $(docker images -q)', capture_output=True, shell=True)

    #SE BORRAN TODAS LAS REDES PERSONALIZADAS
    sp.run('docker network rm $(docker network ls -q)', capture_output=True, shell=True)
    
    #SE CARGA LA IMAGEN QUE SE VA A UTILIZAR
    sp.run(['docker','load','-i','/home/pete/Escritorio/ProyectoTerminal/PT/util/images/ubuntu.tar'],\
                                    capture_output=False)
    
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
    validaNetwork = False
    ip = ''
    gw = ''
    hp = '0'
    msk = 0

    #SE ENVÍA EL COMANDO PARA EVALUAR LA IMAGEN UTILIZADA EN EL CONTENEDOR
    listImagen = ['docker', 'ps', '--filter', 'name=MiNetwork',\
                            '--filter', 'ancestor=ubuntu', '-aq']
    testImagen = sp.run(listImagen, capture_output=True, encoding='utf-8')
    
    if len(testImagen.stdout) > 0:
        validaImagen = True

    #SE ENVÍA EL COMANDO PARA EL INSPECT DEL CONTENEDOR
    output = sp.run(['docker','inspect', 'MiNetwork'], capture_output=True,\
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
                                .get('443/tcp')[0].get('HostPort')

        except TypeError as err:
            err = 'Error: {}'.format(err)
        
        #SE EVALUA LA OPCIÓN DE DETACH
        ain = inspect.get('Config').get('AttachStdin')
        aout = inspect.get('Config').get('AttachStdout')

        if n == '/MiNetwork' and hp == '443' and ain == False and aout == False:
            validaCaracteristicas = True
                
        #SE EVALUA LA NETWORK
        try:
            ip = inspect.get('NetworkSettings').get('Networks').get('miRed')\
                                            .get('IPAddress')

            gw = inspect.get('NetworkSettings').get('Networks').get('miRed')\
                                            .get('Gateway')
            
            msk = inspect.get('NetworkSettings').get('Networks').get('miRed')\
                                            .get('IPPrefixLen')
        except TypeError as err:
            err = 'Error: {}'.format(err)

        if ip == '10.172.14.1' and gw == '10.172.14.6' and msk == 29:
            validaNetwork = True
            
    limpiarEscenario()

    if validaCaracteristicas == True and validaImagen == True and validaNetwork == True:
        resultado = True

    return resultado


def ayudaEjercicio():

    ayuda = """
    Para agregar un contendor a una red, primero debes crearla con el siguiente
    comando:

    \tdocker network create

    Recuerda incluir el ID de la red y la máscara con '/' ejemplo:

    \t192.168.0.0/24

    También recuerda los siguientes comandos de Docker:

    -d \t Modo detach
    -p \t Mapeo de puertos
    
    """

    return ayuda


def respuestaEjercicio():

    respuesta = """
    La siguiente secuencia de comandos da solución al ejercicio: 

    docker network create --subnet 10.172.14.0/29 --gateway 10.172.14.6 miRed
    docker run -dit -p 443:443 --network=miRed --ip 10.172.14.1 --name=MiNetwork ubuntu
    """

    return respuesta


def vistaEjercicio(usuario):
    sp.run('clear')

    logo = logoUAM.printLogo()
    print(logo)
    sentencia = """
    Levanta un contenedor de Ubuntu llamado "MiNetwork" en modo DETACH y con la
    terminal interactiva, con una IP 10.172.14.1 del segmento 10.172.14.0/29 
    de una red que se llame "miRed", el gateway de la red debe ser la IP
    10.172.14.6. Mapear el puerto 443 del host al puerto 443 del contenedor.

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