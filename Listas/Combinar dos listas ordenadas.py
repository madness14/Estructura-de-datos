#Combina dos listas ordenadas en una
#sola lista ordenada.

def llenarlista(n):
    lista = []
    for i in range(n):
        lista.append(input('Ingresa elemento %s: '% (i+1)))
    if not lista:
        print('feo unu')
        exit(1)
    else:
        return lista

def combinarlistas(lista1, lista2):
    nuevlista = lista1 + lista2
    return nuevlista
if __name__=='__main__':
    n1 = int(input('Ingresa el num de elementos feos de la primera lista owo: '))
    n2 = int(input('Ingresa el num de elementos feos pero ahora de la segunda lista owo: '))
    lista1 = llenarlista(n1)
    lista2 = llenarlista(n2)
    print('Nueva lista combinada uwu: ', combinarlistas(lista1, lista2))