import subprocess as sp
import json


def evaluarEjercicio():
    resultado = False
    validaImagen = False
    validaCaracteristicas = False
    validaNetwork = False
    hp = '0'

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
            
        
    if validaCaracteristicas == True and validaImagen == True and validaNetwork == True:
        resultado = True

    return resultado
        


resultado = evaluarEjercicio()
print(resultado)

