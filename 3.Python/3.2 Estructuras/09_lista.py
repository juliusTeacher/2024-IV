# Escribir un programa que pregunte al usuario los números ganadores del miloto, los almacene en una lista y los muestre
# por pantalla ordenados de mayor a menor.

# SOLUCIÓN

numeros_ganadores = []

print ("Ingrese los números ganadores. Para detener, ingrese un valor no numerico o presione ENTER:")

while True:
    try:
        numero = int(input("Ingrese un numero ganador: "))
        numeros_ganadores.append(numero)
    except ValueError:
        break
    numeros_ganadores.sort(reverse=True)
          
print("Numeros ganadores ordenados de mayor a menor:")
print(numeros_ganadores)