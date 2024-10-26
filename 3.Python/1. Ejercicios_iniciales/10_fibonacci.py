# Calcule la suma de términos de la serie de Fibonacci

#SOLUCIÓN
n = int(input('Cantidad: '))
a = 0
b = 1
print('La serie de Fibonacci es: ')
for i in range(n):
    print(a,'|', end='')
    tmp = a + b
    a = b
    b = tmp
    