print('Introduce dos números y el programa dirá cual es el mayor.')
print('----------------------------')
numero_1 = input('Inserta el primer número: ')
numero_2 = input('Inserta el segundo número: ')
print('----------------------------')
if numero_1 < numero_2:
    print(numero_2,'es mayor que',numero_1)
elif numero_1 == numero_2:
    print('Son el mismo número')
else:
    print(numero_1,'es mayor que',numero_2)
print('----------------------------')
