# Planteamiento del problema
# Realice una aplicación de búsqueda de datos personales que realice las siguientes operaciones:
# Agregar persona, buscar persona, eliminar persona y salir.

# SOLUCIÓN
import os
datos_personales = []

def fnt_limpiarcls():
    os.system('cls')

def buscador():
    #Código para realilzar la búsqueda
    identificacion = input('Digite la identificación: ')
    for i in range(len(datos_personales)):
        if(identificacion == datos_personales[i][2]):
            return i

def menu():
    print('\t MENÚ PRINCIPAL')
    print('\t 1- Agregar persona')
    print('\t 2- Buscar persona')
    print('\t 3- Eliminar persona')
    print('\t 4- Salir')
    
control = True
while control:
    fnt_limpiarcls()
    menu()
    opc = int(input('Elija la opción a realizar: '))
    if(opc == 1):
         fnt_limpiarcls()
         print('AGREGAR PERSONA A LA BASE DE DATOS')
         persona = input('Nombre, Apellido, Identificación, edad: ').split(',')
         datos_personales.append(persona)
         input('Registro exitoso, presione <ENTER> para continuar')
    elif(opc == 2):
        fnt_limpiarcls()
        encontrado = buscador()
        if(encontrado != None):
            print(datos_personales[encontrado])
        else:
            print('El usuario no se encuentra registrado en la base de datos')
        input('Presione <ENTER> para continuar')
    elif(opc == 3):
        fnt_limpiarcls()
        encontrado = buscador()
        if(encontrado != None):
            datos_personales.pop(encontrado)
        else:
            print('El usuario no se encuentra en la base de datos')
        input('Presione <ENTER> para continuar')
    elif(opc == 4):
        fnt_limpiarcls()
        print('Gracias por utilizar el programa')
        break
    else:
        print('Error, intente de nuevo')
        input('Presione <ENTER> para continuar')
        