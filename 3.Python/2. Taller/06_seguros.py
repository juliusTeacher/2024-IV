# Seguros Bolívar tiene contratados a N vendedores. Cada uno hace tres ventas a la semana. 
# Su política de pagos es que un vendedor recibe un sueldo base ($1.590.000), y un 10% extra por comisiones de sus ventas. 
# El gerente de su compañía desea saber cuánto dinero obtendrá en la semana cada vendedor por concepto de comisiones por las 
# tres ventas realizadas, y cuanto tomando en cuenta su sueldo base y sus comision

n= int(input("cantidad de vendedores: "))
i = 0
while i <= n:
    vendedor=int(input(f'vendedor #{i+1}: '))
    v1= float(input("venta 1: $"))
    v2= float(input("venta 2: $"))
    v3= float(input("venta 3: $"))
    vt= (v1+v2+v3)
    coms= vt*0.1
    sal= 1590000+coms
    print("salario ttotal del vendedor",i,"es, $",sal)
    i+=1