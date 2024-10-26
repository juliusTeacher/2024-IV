#De una lista de números, obtenga cuántos son positivos, negativos y neutros.

n = int(input('Cantidad de números: '))
cp = 0
cn = 0 
cc = 0
for i in range(n):
    numero = int(input('Numero: '))
    if (numero == 0):
        cc = cc + 1
    else:
        if (numero > 0):
            cp = cp + 1
        else:
            cn = cn + 1

print('Cantidad de positivos: ',cp)
print('Cantidad de negativos: ',cn)
print('Cantidad de neutros: ',cc)