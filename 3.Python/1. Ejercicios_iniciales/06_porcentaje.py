# Tres personas deciden invertir su dinero para formar una empresa. 
# Cada una de ellas invierte una cantidad distinta. Hacer un algoritmo que imprima el porcentaje 
# que cada quien invierte con respecto al total de la inversión.

# SOLUCIÓN
x = float(input('Inversión de la persona 1, $'))
y = float(input('Inversión de la persona 2, $'))
z = float(input('Inversión de la persona 3, $'))

total = x + y + z
print('Total inversion, $',total)

porc_x = (x / total) * 100
porc_y = (y / total) * 100
porc_z = (z / total) * 100

print('La persona 1 obtuvo un porcentaje del: ',porc_x,'%')
print('La persona 2 obtuvo un porcentaje del: ',porc_y,'%')
print('La persona 3 obtuvo un porcentaje del: ',porc_z,'%')