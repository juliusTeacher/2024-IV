# Planteamiento del problema
# Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores), y posterior
# ordene los elementos de mayor a menor.

# SOLUCIÓN
import random
array = []
for i in range(1,11):
    array.append(random.randint(1,10))
array.sort()

for j in array:
    print(j,' ',end='')