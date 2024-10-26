# Un obrero necesita calcular su salario semanal, el cual se obtiene de la siguiente manera: 
# Si trabaja 40 horas o menos se le paga $16 por hora. Si trabaja más de 40 horas se le paga 
# $16 por cada una de las primeras 40 horas y $20 por cada hora extra.


hr = int(input("Digite horas trabajadas: "))
if hr <=40:
    slr=16*hr
    print ("Su salario es de :",slr)
else:
    slr = 16*40
    horas_extras = hr-40
    slrtotal = slr +(20*horas_extras)
    print ("Su salario es de: ",slrtotal)