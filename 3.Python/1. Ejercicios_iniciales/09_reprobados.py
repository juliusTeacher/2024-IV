# Lea N calificaciones de un grupo de alumnos, calcule y escriba el porcentaje de reprobados, 
# tomando en cuenta que la calificación mínima aprobatoria es de 70.

# SOLUCIÓN
n = int(input('Cantidad de alumnos: '))
suma = 0 #acumulador
reprobados = 0 #contador
for i in range(n):
    nota = float(input(f'Nota del alumno {i+1}: '))
    suma +=nota #suma = suma +  nota
    if(nota < 70):
        reprobados +=1 #reprobados = reprobados + 1
promedio = suma / n
reprob = (reprobados / n) * 100
print('Promedio del curso: ',promedio)
print('Reprobados: ',reprobados,' equivalente al: ',reprob,'%')