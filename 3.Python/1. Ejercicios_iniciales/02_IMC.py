#Calcular el IMC (Índice de Masa Corporal) de una persona teniendo en cuenta el rango:
#Peso bajo: < 18.5
#Normal: 18.5 - 24.9
#Sobrepeso: 25 - 29.9
#Obesidad: > 30

#IMC = peso / altura ^2

peso = float(input('Peso (kg): '))
altura = float(input('Estatura (mts): '))
imc = peso / (altura ** 2)

print('IMC = ',imc)
if(imc < 18.5):
    print('Peso bajo')
elif(imc >= 18.5 and imc < 24.9):
    print('Peso normal')
elif(imc >= 25 and imc < 29.9):
    print('Sobrepeso')
else:
    print('Obesidad')