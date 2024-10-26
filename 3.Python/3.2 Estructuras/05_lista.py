# Planteamiento del problema
# Un fanático deportivo registra los resultados de su equipo preferido en una cadena de caracteres donde cada
# posición de la cadena puede contener uno de los siguientes valores:
# P: perdido
# E: empatado
# G: ganado

# Proponga una solución informática que permita al fanático, conocer en el momento que el desee, el puntaje
# de su equipo si sabe que:

# Resultado P   E   G   Otro
# Puntos    0   1   3   0

# SOLUCIÓN
try:
    partido = int(input('Número de partidos: '))
    lista_resultados = []
    contador = 0
    while(contador < partido):
        estado = input('Estado del partido: ').upper() #Método upper => Valor que convierte a mayúsculas
        lista_resultados.append(estado)
        contador +=1
    
    suma = 0
    for i in lista_resultados:
        if(i == 'G'):
            suma +=3
        elif(i == 'E'):
            suma +=1
    print(suma)
except Exception:
    print('Error')