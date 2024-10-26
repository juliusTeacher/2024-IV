import os
os.system('cls')

notas = []
n = int(input('Longitud del array: '))
sumatoria = 0
i = 0
for i in range(n):
    nota = float(input(f'Ingrese la nota[{i+1}]: '))
    notas.append(nota)
    sumatoria += notas[i] # sumatoria = sumatoria + notas[i]

print('Sumatoria: ',sumatoria)
print('Promedio: ',sumatoria / 6)
    
