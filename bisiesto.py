print('Es bisiesto?')
año = input('Año: ')
termina_00 = False
if int(año[2]) + int(año[3]) == 0:
    termina_00 = True
año = int(año)
if termina_00 == True:
    if año % 400 == 0:
        print('Es bisiesto')
    else:
        print('No es bisiesto')
else:
    if año % 4 == 0:
        print('Es bisiesto')
    else:
        print('No es bisiesto')
