import math

a = float(input('A: '))
b = float(input('B: '))
c = float(input('C: '))

det = b**2 - (4*a*c)

if(det == 0):
    x = -b / (2*a)
    print('X = ',x)
else:
    if(det > 0):
        x1 = -b + math.sqrt(det) / (2* a)
        x2 = -b - math.sqrt(det) / (2* a)
        print('X1 = ',x1)
        print('X2 = ',x2)