# Automotores del Litoral premia anualmente a sus mejores asesores comerciales de acuerdo 
# con la siguiente tabla:

# Ventas            Comisión sobre ventas totales
# 1000 <= v < 3000  3%
# 3000 <= v < 5000  4%
# 5000 <= v < 7000  5%
# 7000 <= v         6%

# Diseñar un algoritmo que lea las ventas de N vendedores y que escriba la comisión anual que le 
# corresponda a cada vendedor. Suponer que nadie vende más de 10000 al año.

n = int(input('Cantidad de vendedores: '))
i = 0
total = 0 
while(i < n):
    vt = float(input(f'Venta total del vendedor {i+1}: '))
    total +=vt
    if(total < 3000):
        comision = vt * 0.03
        print('La comisión es de $',comision)
    elif(total < 5000):
        comision = vt * 0.04
        print('La comisión es de $',comision)
    elif(total < 7000):
        comision = vt * 0.05
        print('La comisión es de $',comision)
    else:
        comision = vt * 0.06
        print('La comisión es de $',comision)
    i+=1
print('Ventas totales, $',total)
