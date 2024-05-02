#Calcula la suma de todos los
#elementos en una lista.

def suma(n, lista):
    suma = 0
    for i in range(n):
        lista.append(int(input()))
        suma += lista[i]
    return lista, suma

if __name__=='__main__':
    n = int(input())
    lista = []
    lista, suma = suma(n, lista)
    print('Lista: ', lista, '; Suma: ', suma)
    