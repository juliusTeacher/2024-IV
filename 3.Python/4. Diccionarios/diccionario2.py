id = int(input('Código del estudiante: '))
nombre = input('Tu nombre: ')
edad = int(input('Edad: '))
direccion = input('Driección de residencia: ')
telefono = int(input('Teléfono: '))

estudiante = {'Id':id,'Nombre':nombre,'Edad':edad,'Direccion':direccion,'Teléfono':telefono }
#print(estudiante)
print('El estudiante con el código:',estudiante['Id'],'\n')
print('Se llama: ',estudiante['Nombre'],'\n')
print('tiene: ',estudiante['Edad'],' años,\n')
print('su dirección es: ',estudiante['Direccion'],'\n')
print('y su teléfono: ',estudiante['Teléfono'])