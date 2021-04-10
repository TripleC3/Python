import random
#entradas y variables
run = True
num1 = int(input('Numero entre...: '))
num2 = int(input('y...: '))
solucion = int(random.uniform(num1,num2))
#ordenar mayor y menor
if num1 < num2:
    numTotal = num2 - num1
    mayor = num2
    menor = num1
elif num1 > num2:
    numTotal = num1 - num2
    mayor = num1
    menor = num2
else:
    print('Elige numeros diferentes')
    quit()
#variable
factorSolucion = (solucion - menor) / (mayor - menor)
#bucle principal
while run:
    #entrada de la respuesta y variables
    numRespuesta = int(input('Prueba un numero: '))
    factorRespuesta = (numRespuesta - menor) / (mayor - menor)
    resta = factorRespuesta - factorSolucion

    #distancia de la respuesta a la solucion
    if resta == 0:
        print(f'El número era {solucion}!!!!')
        run = False
    elif resta > 0.80:
        print('MUY abajo')
    elif resta > 0.60:
        print('Muy abajo')
    elif resta > 0.40:
        print('Mas abajo')
    elif resta > 0.20:
        print('Un poco mas abajo...')
    elif resta > 0:
        print('Está casi abajo...')
    elif resta > -0.20:
        print('Está casi arriba...')
    elif resta > -0.40:
        print('Un poco mas arriba...')
    elif resta > -0.60:
        print('Mas arriba')
    elif resta > -0.80:
        print('Muy arriba')
    elif resta > -1:
        print('MUY arriba')
