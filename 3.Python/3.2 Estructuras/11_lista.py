# Se requiere realizar un programa que lea por teclado 5 notas obtenidas por un estudiante(comprendidas entre 0 y 5)
# A continuación debe mostrar todas las notas, el promedio, la nota más alta y la nota menor.

# SOLUCIÓN
notas = []
for i in range(1,6):
    while True:
        nota = int(input(f'Nota {i}: '))
        if(nota >=0 and nota<=5): break
    notas.append(nota)
print('Notas: ',end='')
for nota in notas:
    print(nota,' ',end='')
print()
print('Promedio: ',sum(notas)/len(notas))
print('Nota máxima: ',max(notas))
print('Nota mínima: ',min(notas))