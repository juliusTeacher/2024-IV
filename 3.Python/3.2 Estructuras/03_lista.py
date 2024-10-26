valores = []
c = []
i = 0

n =int(input('Dimensión del array: '))
for i in range(n):
    numero = int(input(f'Ingrese el {i+1} número: '))
    valores.append(numero)
    c.append(numero ** 2)
    
print('Resultados del array: ')
for i in range(n):
    print('El número ',valores[i],' elevado al cuadrado es: ',c[i])
