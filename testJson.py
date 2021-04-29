import subprocess as sp
import json


def evaluarEjercicio():
    resultado = False
    validaImagen = False
    validaCaracteristicas = False
    hp = '0'

    #SE ENVÍA EL COMANDO PARA EVALUAR LA IMAGEN UTILIZADA EN EL CONTENEDOR
    listImagen = ['docker', 'ps', '--filter', 'name=MiPrueba',\
                            '--filter', 'ancestor=debian', '-aq']
    testImagen = sp.run(listImagen, capture_output=True, encoding='utf-8')
    
    if len(testImagen.stdout) > 0:
        validaImagen = True

    #SE ENVÍA EL COMANDO PARA EL INSPECT DEL CONTENEDOR
    output = sp.run(['docker','inspect', 'MiPrueba'], capture_output=True,\
                                                            encoding='utf-8')    

    #SE EVALUA QUE SE HAYA COLOCADO CORRECTAMENTE EL NOMBRE DEL CONTENEDOR
    if output.stdout == '[]\n':
        print(output.stdout)
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
        

        if n == '/MiPrueba' and hp == '80' and ain == False and aout == False and\
            h == 'iot' and r == 'unless-stopped' and t == 'TZ=America/Mexico_City':
            validaCaracteristicas = True

        
    if validaCaracteristicas == True and validaImagen == True:
        resultado = True

    return resultado
        


resultado = evaluarEjercicio()
print(resultado)

