# Diseñar un algoritmo que calcule el promedio de notas del 
# primer parcial de un curso de N estudiantes.

n = int(input('Cantidad de notas: '))
i = 1
suma = 0
while(i <= n):
    nota = float(input('Digite su nota: '))
    suma += nota #suma = suma + nota
    i+=1

promedio = suma / n
print('Promedio: ',promedio)
