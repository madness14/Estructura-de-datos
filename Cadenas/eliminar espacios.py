# Elimina los espacios en blanco de
# una cadena.

def noespacios(x):
    xnoesp = x.replace(' ', '')
    return xnoesp

if __name__=='__main__':
    x = input('Ingresa alguna oracion uwu: ')
    print('Frase sin espacios: ', noespacios(x))