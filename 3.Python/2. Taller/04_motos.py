# Una distribuidora de motocicletas tiene una promoción de fin de año que consiste en lo siguiente. 
# Las motos marca Honda tienen un descuento del 5%, las marcas Yamaha del 8% y las Suzuki del 10%, las otras marcas 2%. 
# Se debe mostrar el precio de la moto, el descuento y el precio a pagar.

Tipo = int(input('Ingrese el tipo de moto, 1= Honda, 2 = yamaha, 3 = Suzuki, 4 = Otras marcas '))

precio= float(input('Ingrese el valor de la moto, '))

if (Tipo==1):
    descuento = precio * 0.05
  
elif (Tipo==2):
    descuento = precio * 0.08
    
elif (Tipo==3):
    descuento = precio * 0.1
    
else:
    descuento = precio * 0.02
    
print("El precio de la moto es: $",precio)
print("El descuento es de: $",descuento)
print("El total a pagar es: $",precio-descuento)


    
