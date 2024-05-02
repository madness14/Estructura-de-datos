# Dada una lista de nombres, crea una
# nueva lista que contenga solo los 
# nombres que comienzan con una letra 
# específica.

def llenarlista(n):
    lista = []
    for i in range(n):
        lista.append(input('Ingresa elemento %s: '% (i+1)))
    if not lista:
        print('feo unu')
        exit(1)
    else:
        return lista

def letraesp(lista, letra):
    listanueva = []
    for i in range(len(lista)):
        for j in range(len(lista[i])):
           if lista[i][j][0]==letra:
               listanueva.append(lista[i])
               break
    if not listanueva:
        return 'Ningun elemento encontrado'
    else:
        return listanueva        
    
if __name__=='__main__':
    n = int(input('Ingresa el num de elementos feos owo: '))
    lista = llenarlista(n)
    letra = input('Ingresa la letra a buscar: ')
    print('Nueva lista con la letra solicitada: ', letraesp(lista, letra))