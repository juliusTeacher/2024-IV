# Leer dos enteros A y B y calcular F de acuerdo a las siguientes reglas:
# F = 2 * A + B, Si A^2 - B^2 < 0
# F = A^2 - 2 * B, Si A^2 - B^2 = 0
# F = A + B, Si A^2 - B^2 > 0

# SOLUCIÓN

a = int(input('A: '))
b = int(input('B: '))

if(a**2 - b**2 < 0):
    f = 2 * (a + b)
elif(a** 2 - b**2 == 0):
    f = (a**2) - (2*b)
elif(a** 2 - b**2 > 0):
    f = a + b
else:
    print('No se puede evaluar las variables A y B')

print('F = ',f)