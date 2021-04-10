import subprocess, time

x = 0
string = subprocess.check_output('tasklist /fo list').decode('Windows-1252').split('\n')
for line in string:
    if 'Uso de memoria' in line:
        x += int(line.split(':')[1].strip()[:-3].replace('.',''))
print(f'\n\n\tTotal: 8084 MB\n\n\tUsando: {x // 1000} MB\n\n\tDisponible: {8084 - x // 1000} MB')
time.sleep(10)
