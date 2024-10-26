# Menú principal, opciones
import os

def menu():
    print('1- Nuevo Abogado')
    print('2- Asignar caso')
    print('3- Nuevas evidencias')
    print('4- Salir del sistema')

def fnt_limpiarcls():
    os.system('cls')

# Programa principal    
listaAbogados = []
validarReg = False
control = True
while control:
    fnt_limpiarcls()
    menu()
    opc = int(input('Elija la opción a realizar: '))
    if(opc == 1):
        if(validarReg == False):
            fnt_limpiarcls()
            print('\n=== REGISTRO DE ABOGADOS ===')
            nombre = str(input('Nombre: '))
            contacto = str(input('Contacto: '))
            especialidad = str(input('Especialidad: '))
            id = int(input('Codigo: '))
            listaAbogados = [nombre, contacto, especialidad, id]
            enter = input('\nRegistro Exitoso')
            validarReg = True
        else:
            enter = input('Ya se encuentra registrado el abogado. Presione <ENTER> para continuar')
    if(opc == 2):
        if(validarReg == True):
            fnt_limpiarcls()
            print('\n=== ACTUALIZAR INFORMACIÓN ===')
            seleccion = int(input('1.Nombre\n2.Contacto\n3.Especialidad\n-> '))
            if(seleccion == 1):
                aux_nombre = str(input('Nombre: '))
                if(aux_nombre == ''):
                    enter = input('Error, Digite el nombre. <ENTER>')
                else:
                    listaAbogados[0] = aux_nombre
                    enter = input('El nombre se actualizó con éxito. <ENTER>')
            if(seleccion == 2):
                aux_contacto = input('Ingrese el nuevo contacto: ')
                if(aux_contacto == ''):
                    enter = input('Error, digite el contacto. <ENTER>')
                else:
                    listaAbogados[1] = aux_contacto
                    enter = input('El contacto ha sido actualizado. <ENTER>')
            if(seleccion == 3):
                aux_especialidad = input('Ingrese la nueva especialidad: ')
                if(aux_especialidad == ''):
                    enter = input('Error, digite la especialidad. <ENTER>')
                else:
                    listaAbogados[2] = aux_especialidad
                    enter = input('La especialidad ha sido actualizada .<ENTER>')
        else:
            enter = input('Debe realizar el registro primero. <ENTER>')
    if(opc == 4):
        print('FIN')
        break
    else:
        input('Error, intente de nuevo, <ENTER>')

        
