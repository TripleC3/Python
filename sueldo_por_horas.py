print('Calculador de sueldo')
print('-------------------------')
try:
    horas = float(input('Horas mensuales: '))
    sueldo = float(input('Euros por hora: '))
except:
    print('Solo se aceptan números, vuelve a intentarlo')
    quit()
print('-------------------------')
if horas <= 40.0 :
    print('Te corresponden:',horas * sueldo)
else:
    print('Has trabajado',horas - 40,'horas extra a',sueldo * 1.75,'euros la hora')
    extra = (horas - 40) * (sueldo * 1.75)
    print('Te corresponden:',horas * sueldo + extra)
print('-------------------------')
