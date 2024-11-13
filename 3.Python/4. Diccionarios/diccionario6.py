# Escribir un programa que gestione las facturas pendientes de cobro de una empresa. 
# Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura 
# y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, 
# pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y 
# su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se 
# eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada 
# hasta el momento y la cantidad pendiente de cobro.

# SOLUCIÓN
import os
 
# Menú principal
def menu():
    print('MENÚ PRINCIPAL')
    print('1 - Agregar factura')
    print('2 - Pagar factura')
    print('3 - Salir')

def limpiar_cls():
    os.system('cls')
    
facturas = {}
bandera = "s"
pendiente = 0
cobrado = 0

while bandera == "s":
    limpiar_cls()
    menu()
    opc = int(input('Escoja la acción a realizar: '))
    if(opc == 1):
        print('AGREGAR FACTURA')
        codigo_fact = int(input('Factura No. '))
        valor = float(input('Costo total de la factura, $'))
        facturas[codigo_fact] = valor
        pendiente +=valor
        print('Pendiente: $'+str(pendiente))
        print('Cobrado el día de hoy: $'+str(cobrado))
        enter = input('Digite <ENTER> para continuar')
    elif(opc == 2):
        print('PAGAR FACTURA')
        codigo_fact = int(input('Factura No. '))
        if codigo_fact in facturas:
            pendiente -= facturas[codigo_fact]
            cobrado += facturas[codigo_fact]
        else:
            print('ERROR: No se encontró la factura con el código'+str(codigo_fact))
        print('Pendiente: $'+str(pendiente))
        print('Cobrado el día de hoy: $'+str(cobrado))
        enter = input('Digite <ENTER> para continuar')
    elif(opc == 3):
        print('Pendiente: $'+str(pendiente))
        print('Cobrado el día de hoy: $'+str(cobrado))
        bandera == "n"
        break