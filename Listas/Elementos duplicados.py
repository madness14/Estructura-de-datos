# Elimina los elementos duplicados 
# de una lista.

def llenarlista(n):
    lista = []
    for i in range(n):
        lista.append(input('Ingresa elemento %s: '% (i+1)))
    if not lista:
        print('feo unu')
        exit(1)
    else:
        return lista

def elementos(lista):
    rep = []
    nuevalista = []
    for elemento in lista:
        if elemento not in nuevalista:
            nuevalista.append(elemento)
        else:
            rep.append(elemento)
    if not rep:
        return 'Ningún elemento encontrado :c', nuevalista
    else:
        return ', '.join(rep), nuevalista

if __name__=='__main__':
    n = int(input('Ingresa el num de elementos feos owo: '))
    lista = llenarlista(n)
    elementosremovidos, nuevlista = elementos(lista)
    print('Palabras repetidas: ', elementosremovidos, '\n', 'Lista sin palabras repetidas: ', nuevlista)
