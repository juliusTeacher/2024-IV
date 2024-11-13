# Se desea almacenar los datos de 3 alumnos. Definir un diccionario cuya clave sea el número de documento del alumno. 
# Como valor almacenar una lista con componentes de tipo tupla donde almacenamos nombre de materia y su nota.
# Crear las siguientes funciones:
# 1) Carga de los alumnos (de cada alumno solicitar su dni y los nombres de las materias y sus notas)
# 2) Listado de todos los alumnos con sus notas
# 3) Consulta de un alumno por su dni, mostrar las materias que cursa y sus notas.

# SOLUCIÓN

# Funciones
def cargar():
    alumnos = {}
    for i in range(3):
        id = int(input('Ingrese su identificación: '))
        asignaturas = []
        continuar = "s"
        while continuar == "s":
            asginatura = input('Asignatura que cursa: ')
            nota = float(input('Nota: '))
            asignaturas.append((asginatura,nota))
            continuar = input('¿Desea cargar otra asignatura para el alumno? [SI/NO]: ')
        alumnos[id] = asignaturas
    return alumnos
    
def listado(alumnos):
    for id in alumnos:
        print('Identificación: ',id)
        print('Asignaturas: ')
        for nota,asignatura in alumnos[id]:
            print(asignatura,nota)

def consulta_notas(alumnos):
    id = int(input('Digite la identificación a consultar: '))
    if id in alumnos:
        for nota,asignatura in alumnos[id]:
            print(asignatura,nota)
    
# Programa principal
alumnos = cargar()
listado(alumnos)
consulta_notas(alumnos)

