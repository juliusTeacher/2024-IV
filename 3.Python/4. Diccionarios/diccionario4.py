# Escribir un programa que cree un diccionario simulando una cesta de la compra. 
# El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida 
# terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato

# Lista de la compra	
# Artículo 1	Precio
# Artículo 2	Precio
# Artículo 3	Precio
# …	            …
# Total	        Coste

# SOLUCIÓN

cesta = {}
continuar = True
while continuar:
    articulo = input('Digite un artículo: ')
    precio = float(input('Precio del '+ articulo +'$ '))
    cesta[articulo] = precio
    continuar =input('¿Desea usted añadir mas artículos a la lista (SI/NO)? ') == "SI"
total_compra = 0
print('Factura de compra-venta')
for articulo, precio in cesta.items():
    print(articulo,'\t', precio)
    total_compra += precio #total_compra = total_compra + precio
print('El total de la compra es, $',total_compra) 