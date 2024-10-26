# Desarrollar un algoritmo que calcule el salario neto que debe recibir un vendedor de un almacén. 
# Se debe tener en cuenta si tiene derecho o no al auxilio de transporte. Para el desarrollo del ejercicio tenga en cuenta las siguientes fórmulas:
# • Sueldo devengado = salario básico * días laborados / 30
# • Días laborados = debe ser entre 1 y 30
# • Auxilio de transporte: Lo reciben los empleados cuyo salario básico sea menor o igual a 2 SMLV.
# • SMLV (2024): $1.300.000
# • Auxilio de Transporte: $162.000 * días laborados / 30
# • Comisión de ventas: En la empresa se tiene estipulado dar una comisión de ventas del 2% sobre las ventas del mes de cada vendedor.
# • Total devengado = sueldo devengado + comisión de ventas
# • Total deducciones = descuentos por préstamos
# • Salario Neto = Total devengado – Total deducciones
# Como resultado del ejercicio se debe imprimir en pantalla lo siguiente:
# Cédula No. XXXXXXXXX
# Empleado: XXXXXXXXXX
# Salario básico, $XXXXXXX
# Auxilio de transporte, $XXXXXXXX
# Comisión de ventas, $XXXXXXXXX
# Préstamos, $XXXXXXXXXXX
# Salario neto a recibir: $XXXXXXXX

SMLV = 1300000
Aux = 162000
Comision = 0.02

Cedula = int(input("Escriba la cedula : "))
Nombre = str(input("Escriba el nomnbre: "))
Ventas = int(input("Numero de ventas: "))
Prestamos = int(input("Prestamos:"))
Salario = int(input("Escriba el salario: "))
Diaslaborados = int(input("Dias laborados: "))

if Diaslaborados > 30:
    print("Los dias no deben ser mayor a 30...")
    
SalarioN = Salario * Diaslaborados

if SalarioN <= (SMLV * 2):
    SalarioN = SalarioN + Aux
    print(SalarioN)
    
Sal_Dev = ((SalarioN * 0.02) + SalarioN)
SalarioNeto = Sal_Dev - Prestamos

print("cc: ", Cedula)
print("Empleado: ", Nombre)
print("Salario basico: ", SalarioN)
if SalarioN <= (SMLV * 2):
    print("AUX DE TRANSPORTE", Aux)
else:
    print("No aplica el auxilio")
print("Comision: ", SalarioN * Comision)
print("Descuento por prestamo ", Prestamos)
print("Salario total ", SalarioNeto)

