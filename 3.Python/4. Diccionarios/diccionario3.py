# FRUTA     PRECIO
# Manzana   1300
# Aguacate  2000
# Melón     1400
# Guineo    3200

# SOLUCIÓN
frutas = {'Manzana': 1300, 'Aguacate': 2000, 'Melón': 1400, 'Guineo': 3200}
fruta = input('¿Qué fruta desea usted? ').title()
kg = float(input('¿Cuántos kilos? '))
if fruta in frutas:
    print(kg,' kilos de:', fruta,' tiene un costo de $',frutas[fruta]*kg)
else:
    print('Lo sentimos, esta fruta no se encuentra disponible')