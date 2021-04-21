import subprocess as sp

def clear():
    '''
        Funcion que limpia el escenario al inicio y al final de los ejercicios
    '''
    #Deleting all containers
    p1 = sp.run('docker rm -f $(docker ps -aq)', capture_output=True, shell=True)
    #Deleting all images
    p2 = sp.run('docker rmi -f $(docker images -q)', capture_output=True, shell=True)

def res1():
    return 'Docker stop $(docker ps -aq)'

def evaluate1():
    '''
        Función que evalúa el ejercicio Nivel 1
    '''
    check = sp.run(['docker','ps','-q'], capture_output=True, encoding='utf-8')
    clear()
    return -1 if len(check.stdout) > 0 else 0

def level1():
    '''
        Función creadora del escenario nivel 1
    '''
    clear()
    #Load image
    sp.run(['docker','load','-i','images/ubuntu.tar'], capture_output=True)
    print('[ Nivel 1 ] Intenta DETENER todos los contenedores en un sólo Comando')
    input('Continuar...')
    sp.run(['clear'])
    print('\n\nPreparando tu escenario...')

    for i in range(10):
        sp.run(['docker','run','-dit','ubuntu'], capture_output=True)
    sp.run(['docker','ps'], capture_output=False, encoding='utf-8')
    print()
    cmd = input('\nTuPrompt$ ')
    sp.run(cmd, capture_output=False, encoding='utf-8', shell=True)
    return evaluate1()

def res2():
    return 'Docker rm -f $(docker ps -aq)'

def evaluate2():
    '''
        Función que evalúa el Nivel 2
    '''
    check = sp.run(['docker','ps','-aq'], capture_output=True, encoding='utf-8')
    clear()
    return -1 if len(check.stdout) > 0 else 0

def level2():
    '''
        Función que crea el Nivel 2
    '''
    clear()
    sp.run(['docker','load','-i','images/ubuntu.tar'], capture_output=True)
    print('[ Nivel 2 ] Intenta ELIMINAR todos los contenedores en UN sólo Comando')
    input('Continuar ... ')
    sp.run(['clear'])
    print('\n\nPreparando tu escenario')
    for i in range(3):
        sp.run(['docker','run','-dit','ubuntu'], capture_output=True)
        sp.run(['docker','run','-d','ubuntu'], capture_output=True)
    
    sp.run(['docker','ps','-a'], capture_output=False, encoding='utf-8')
    print()
    cmd = input('TuPrompt$')
    sp.run(cmd, capture_output=False, encoding='utf-8', shell=True)
    return evaluate2()

def res3():
    return 'docker rm -f $(docker ps -aq) && docker rmi $(docker images -q)'

def evaluate3():
    '''
        Función que evalúa el Nivel 3
    '''
    check1 = sp.run(['docker','images', '-q'], capture_output=True, encoding='utf-8')
    check2 = sp.run(['docker','ps', '-aq'], capture_output=True, encoding='utf-8')
    clear()
    return -1 if len(check1.stdout)>0 and len(check2.stdout)>0 else 0

def level3():
    '''
        Función que crea el Nivel 3
    '''
    clear()
    sp.run(['docker','load','-i','images/ubuntu.tar'], capture_output=True)
    print('[ Nivel 3 ] Elimina la imagen de ubuntu y TODOS los contenedores en UN solo comando')
    input('Continuar ... ')
    sp.run(['clear'])
    print('\n\nPreparando tu escenario')
    for i in range(2):
        sp.run(['docker','run','-dit','ubuntu'], capture_output=True)
    
    print('\n* Contenedores actualmente activos')
    sp.run(['docker','ps','-a'], capture_output=False, encoding='utf-8')
    print('\n* Imágenes actualmente cargadas')
    sp.run(['docker', 'images'])
    print()
    cmd = input('TuPrompt$')
    sp.run(cmd, capture_output=False, encoding='utf-8', shell=True)
    return evaluate3()
    