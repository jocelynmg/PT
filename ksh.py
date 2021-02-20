import sys, subprocess

"""
proceso = subprocess.Popen(['sudo docker ps -a'], stdout=subprocess.PIPE, shell=True)
proceso.wait()
salida = proceso.stdout.read()
proceso.stdout.close()
salida = salida.decode(sys.getdefaultencoding())
print(salida)

print(type(salida))

listSalida = salida.split('\n')

resultado = False

for line in listSalida:

    if 'python' in line and '\"sleep 5\"' in line and 'PythonTest' in line:
        print(line)
        resultado = True

if resultado == True:
    print('¡Ejercicio Correcto!')
else:
    print('¡Resultado incorrecto!, intenta otra vez')
"""


#SE RECUPERAN LOS IDS DE LOS DOCKER EN ESTADO EXITED
proceso = subprocess.Popen('docker ps -aq'.split(), stdout=subprocess.PIPE)
proceso.wait()
ids = proceso.stdout.read()
proceso.stdout.close()
ids = ids.decode(sys.getdefaultencoding()).split()

#SE LIMPIAN LOS CONTENEDORES QUE SE HAYAN EJECUTADO
for id in ids:
    subprocess.Popen(f'docker rm {id}'.split())
