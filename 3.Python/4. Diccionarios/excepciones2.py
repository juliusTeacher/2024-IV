# Manejo de las excepciones
# Calculadora básica

def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    return a / b

def menu():
    print('1. SUMA')
    print('2. RESTA')
    print('3. MULTIPLICACIÓN')
    print('4. DIVISIÓN')
    
# Programa principal
while True:
    try:
        num1 = float(input('Número 1: '))
        num2 = float(input('Número 2: '))
        menu()
        opc = int(input('Elija la operación a realizar: '))
        if(opc == 1):
            print('Suma: ',suma(num1, num2))
            break
        elif(opc == 2):
            print('Resta: ',resta(num1, num2))
            break
        elif(opc == 3):
            print('Multiplicación: ',multiplicacion(num1, num2))
            break
        elif(opc == 4):
            print('División: ',division(num1, num2))
            break
        else:
            print('Opción inválida')
    except ZeroDivisionError:
        print('Valor indeterminado')
    except:
        print('Error')
        opc = '?'