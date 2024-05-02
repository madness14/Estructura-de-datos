# Dada una lista de palabras,
# imprime todas las palabras
# que tienen más de 5 letras.

def palabras(n, lista):
    palabras = ''
    if not n:
        print('unu malo')
        exit()
    for i in range(n):
        lista.append(input('Palabra: '))
        if len(lista[i]) >= 5:
            palabras += lista[i] + ', '
    if not palabras:
        return 'Ninguna palabra encontrada unu'
    else:
        return palabras[:-2]

if __name__=='__main__':
    n = int(input('Ingresa el num de elementos en la lista fea: '))
    lista = []
    print('Las palabras que tienen mas de 5 letras son: ', palabras(n, lista))