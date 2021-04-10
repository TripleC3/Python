import subprocess

wifis = []
comando = subprocess.check_output('netsh wlan show profiles').decode('utf-8').split('\n')
for line in comando:
    if 'Perfil de todos los usuarios' in line:
        wifis.append(line.split(':')[1][1:-1])
        
print('Claves encontradas:\n')
for wifi in wifis:
    comando = subprocess.check_output(f'netsh wlan show profile "{wifi}" key=clear').decode('utf-8', errors='ignore').split('\n')
    for line in comando:
        if 'Contenido de la clave' in line:
            print(f'Wifi: {wifi}\nPassword: {line.split(":")[1][1:-1]}')
