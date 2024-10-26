# Haga un programa que realice un menú principal y realice las operaciones matemáticas básicas y complejas
# (potenciación, radicación, ecuación de primer grado)

# SOLUCIÓN

# FUNCIONES MATEMÁTICAS BÁSICAS

def suma(x,y):
    return x + y

def resta(x,y):
    return x - y

def multiplicacion(x,y):
    return x * y;

def division(x,y):
    if(y == 0):
        return 'Error, no se puede dividir por cero!!'
    else:
        return x / y
    
# FUNCIONES MATEMÁTICAS COMPLEJAS (Potencia, raíz, Ecuación de primer grado)
def potencia(x,y):
    return x ** y

def raiz(x,y):
    return x ** (1/y)

def ecuacion(x,y):
    if(y == 0):
        return 'Error'
    else:
        return -y / x
    
# MENU PRINCIPAL
def menu():
    print('1 - SUMA')
    print('2 - RESTA')
    print('3 - MULTIPLICACION')
    print('4 - DIVISION')
    print('5 - POTENCIA')
    print('6 - RAÍZ')
    print('7 - ECUACIÓN DE PRIMER GRADO')
    


# PROGRAMA PRINCIPAL
while True:
    menu()
    op = int(input('Escoja la opción: ')) 
    if(op == 1):
        numero_1 = int(input('Número 1: '))
        numero_2 = int(input('Número 2: '))
        print('La suma es: ',suma(numero_1, numero_2))
    elif(op == 2):
        numero_1 = int(input('Número 1: '))
        numero_2 = int(input('Número 2: '))
        print('La resta es: ',resta(numero_1, numero_2))
    elif(op == 3):
        numero_1 = int(input('Número 1: '))
        numero_2 = int(input('Número 2: '))
        print('La multiplicación es: ',multiplicacion(numero_1, numero_2))
    elif(op == 4):
        numero_1 = int(input('Número 1: '))
        numero_2 = int(input('Número 2: '))
        print('La división es: ',division(numero_1, numero_2))
    elif(op == 5):
        base = int(input('Base: '))
        exponente = int(input('Exponente: '))
        print('La potencia de ',base,' elevado a la', exponente,' es: ',potencia(base,exponente))
    elif(op == 6):
        radicando = float(input('Radicando: '))
        indice = float(input('Índice: '))
        print('La raíz es: ',raiz(radicando,indice))
    elif(op == 7):
         a = float(input('A: '))
         b = float(input('B: '))
         print('El valor de la ecuación, X=',ecuacion(a,b))
    else:
        print('Bye')
        break
