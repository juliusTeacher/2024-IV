while(True):     
    try:
        a = int(input('Número: '))
        b = 4
        print('{}/{} = {}'.format(a,b,a/b))
    except:
        print('Error, introduzca un valor numérico')
    else:
        print('La aplicación está funcionando correctamente')
        break
    finally:
        print('Fin de la iteracion')