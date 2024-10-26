# Escribir un programa que almacene las asignaturas de un curso(por ejemplo, Matemáticas, Programación, Estadística,
# Química, Historia y Geografía) en una lista, pregunte al usuario la calificación que ha sacado en cada asignatura
# y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar en pantalla las asignaturas que
# el usuario tiene que repetir.

# SOLUCIÓN
asignaturas = ["Matematicas", "Programacion", "Estadistica", "Quimica", "Historia", "Geografia"]
aprobadas = []

for i in asignaturas:
    calificacion = float(input("Calificacion de"+ i +": "))
    if calificacion >=5:
        aprobadas.append(i)
for i in aprobadas:
    asignaturas.remove(i)
print('Usted debe repetir la(s) siguiente(s) asignatura(s): ',str(asignaturas))