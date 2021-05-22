import subprocess as sp
import json

def prepararEjercicio():

    #SE ELIMINAN TODOS LOS CONTENEDORES
    sp.run('docker rm -f $(docker ps -aq)', capture_output=True, shell=True)

    #SE ELIMINAN TODAS LAS IMAGENES
    sp.run('docker rmi -f $(docker images -q)', capture_output=True, shell=True)

    #SE CARGA LA IMAGEN QUE SE VA A UTILIZAR
    sp.run(['docker','load','-i','/home/pete/Escritorio/ProyectoTerminal/PT/util/images/base.tar'],\
                                            capture_output=False)
    
    #SE EJECUTA EL DOCKERFILE
    sp.run(['docker', 'build', '-f', '/home/pete/Escritorio/ProyectoTerminal/PT/util/dockerfile', '.'],\
                                            capture_output=True)

    sp.run(['docker', 'rmi', 'base'], capture_output=True)
    
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
        

#prepararEjercicio()
resultado = evaluarEjercicio()
print(resultado)

