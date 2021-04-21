import sys, logoUAM
from time import sleep
import subprocess as sp

def prepararEjercicio():
    '''
        Funcion que limpia el escenario al inicio y al final de los ejercicios
    '''
    #Deleting all containers
    sp.run('docker rm -f $(docker ps -aq)', capture_output=True, shell=True)
    #Deleting all images
    sp.run('docker rmi -f $(docker images -q)', capture_output=True, shell=True)

def respuestaEjercicio():
    return 'Docker stop $(docker ps -aq)'

def evaluarEjercicio():
    '''
        Función que evalúa el ejercicio Nivel 1
    '''
    check = sp.run(['docker','ps','-q'], capture_output=True, encoding='utf-8')
    prepararEjercicio()
    return False if len(check.stdout) > 0 else True

def vistaEjercicio(usuario):
    '''
        Función creadora del escenario nivel 1
    '''
    prepararEjercicio()
    #Load image
    sp.run(['docker','load','-i','/home/pete/Escritorio/ProyectoTerminal/PT/\
                    util/images/ubuntu.tar'], capture_output=True)

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

    resultado = evaluarEjercicio()

    resultadoEjercicio = [usuario, resultado]
    sleep(2)

    return resultadoEjercicio
