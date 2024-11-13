# Cree una lista de elementos y lo guarde en un archivo en formato de texto (.*txt)

f = open('lista.txt','w')
array = ['Manzana', 'Pera', 'Piña', 'Patilla', 'Naranja']

for i in array:
    f.write(i + '\n')

f.close()