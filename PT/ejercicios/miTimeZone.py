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
    sp.run(['docker','load','-i','/home/pete/Escritorio/ProyectoTerminal/debian.tar'],\
                                    capture_output=False)
    
    return True


def limpiarEscenario():

    #SE ELIMINAN TODOS LOS CONTENEDORES
    sp.run('docker rm -f $(docker ps -aq)', capture_output=True, shell=True)

    #SE ELIMINAN TODAS LAS IMAGENES
    sp.run('docker rmi -f $(docker images -q)', capture_output=True, shell=True)

    return True


def evaluarEjercicio():
    resultado = False
    validaImagen = False
    validaCaracteristicas = False
    hp = '0'

    #SE ENVÍA EL COMANDO PARA EVALUAR LA IMAGEN UTILIZADA EN EL CONTENEDOR
    listImagen = ['docker', 'ps', '--filter', 'name=MiTimeZone',\
                            '--filter', 'ancestor=debian', '-aq']
    testImagen = sp.run(listImagen, capture_output=True, encoding='utf-8')
    
    if len(testImagen.stdout) > 0:
        validaImagen = True

    #SE ENVÍA EL COMANDO PARA EL INSPECT DEL CONTENEDOR
    output = sp.run(['docker','inspect', 'MiTimeZone'], capture_output=True,\
                                                            encoding='utf-8')    

    #SE EVALUA QUE SE HAYA COLOCADO CORRECTAMENTE EL NOMBRE DEL CONTENEDOR
    if output.stdout == '[]\n':
        return False

    else:
        #SE OBTIENE UN DICCIONARIO DEL COMANDO DOCKER INSPECT
        inspect = json.loads(output.stdout)[0]
        
        #SE EVALUA NAME, HOSTNAME, RESTART POLICY, TIME_ZONE
        n = inspect.get('Name')
        h = inspect.get('Config').get('Hostname')
        r = inspect.get('HostConfig').get('RestartPolicy').get('Name')
        t = inspect.get('Config').get('Env')[0]

        #SE EVALUA LA OPCIÓN DE DETACH
        ain = inspect.get('Config').get('AttachStdin')
        aout = inspect.get('Config').get('AttachStdout')
        
        #SE EVALUA TANTO EL EXPOSED PORT COMO EL HOST PORT
        try:
            hp = inspect.get('NetworkSettings').get('Ports')\
                                .get('80/tcp')[0].get('HostPort')

        except TypeError as err:
            err = 'Error: {}'.format(err)
        

        if n == '/MiTimeZone' and hp == '80' and ain == False and aout == False and\
            h == 'iot' and r == 'unless-stopped' and t == 'TZ=America/Mexico_City':
            validaCaracteristicas = True

    #SE MANDA A LIMPIAR EL ESCENARIO
    limpiarEscenario()
        
    if validaCaracteristicas == True and validaImagen == True:
        resultado = True

    return resultado


def ayudaEjercicio():

    ayuda = """
    + Recuerda que para cambiar la zona horaria del contenedor debes enviar la 
      siguiente variable de entorno.

        TZ

    + Toma en cuenta las siguientes banderas de Docker:

        -d \t Modo detach
        -p \t Mapeo de puertos
        -h \t Hostname
        --restart  Política de reinicio
    
    + Al nombrar el contenedor, toma en cuenta mayúsculas y minúsculas.

    """

    return ayuda


def respuestaEjercicio():

    respuesta = """
    + El siguiente comando da solución al ejercicio:

        docker run -dit --name MiTimeZone -h iot -p 80:80 --restart=unless-stopped -e TZ="America/Mexico_City" debian
    """

    return respuesta


def vistaEjercicio(usuario):
    sp.run('clear')

    logo = logoUAM.printLogo()
    print(logo)
    sentencia = """
    Levanta un contenedor usando una imagen de Debian llamado "MiTimeZone" en
    modo DETACH y con la terminal interactiva, con zona horaria de la Ciudad 
    de México (America/Mexico_City) y con una política de reinicio hasta que 
    alguien lo detenga. Mapea el puerto 80 del host al puerto 80 del contenedor. 
    El hostname del contenedor debe ser "iot".

    Escribe 'exit' cuando hayas finalizado o en cualquier otro momento para 
    regresar a la aplicación principal.
    """
    print(sentencia)

    input('Da enter para cargar tu escenario...')

    #SE LLAMA A LA FUNCIÓN PARA PREPARAR EL EJERCICIO
    prepararEjercicio()
    
    #ENTRANDO A KORN SHELL
    print('\nAhora estás en KornShell')
    sp.call('ksh')

    #UNA VEZ QUE EL USUARIO ENTRA EXIT EN LA TERMINAL, SE EVALUA EL EJERCICIO
    print('\nEvaluando ejercicio...')

    resultado = evaluarEjercicio()

    #SE DECLARA LA LISTA CON EL USUARIO Y EL RESULTADO
    resultadoEjercicio = [usuario, resultado]
    sleep(2)

    return resultadoEjercicio