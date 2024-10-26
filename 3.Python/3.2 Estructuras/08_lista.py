# Crea un programa que pida un número al usuario de mes(por ejemplo, el 4) y diga cuántos días tiene(por ejemplo 30)
# y el nombre del mes. Debes usar listas. Para simplificarlo vamos a suponer que febrero tiene 28 días.

# SOLUCIÓN
dias = [31,28,31,30,31,30,31,31,30,31,30,31]
meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'] 

control = True
while control:
    mes = int(input('Ingrese el mes(1-12): '))
    if(mes < 1 or mes > 12):
        print('Mes incorrecto, ingrese de nuevo!')
    if(mes >=1 and mes <=12): 
        break
print('El mes de',meses[mes-1],'tiene:',dias[mes-1],'días')