# Implementa un algoritmo de ordenamiento 
# de lista (por ejemplo, burbuja, 
# selección, inserción) desde cero.

def llenarlista(lista):
    for i in range(10):
        lista.append(input('Valor %s: ' %(i+1)))
    if not lista:
        print('feo unu')
        exit(1)
    else:
        return lista
    
def burbuja(lista):
    copia = lista.copy()
    n = len(copia)
    for i in range(n-1):       
        for j in range(n-1-i): 
            if copia[j] > copia[j+1]:
                temp = copia[j]
                copia[j] = copia[j+1]
                copia[j+1] = temp
    return copia

if __name__=='__main__':
    lista = []
    print('Ingresa 10 numeros para ser ordenados')
    lista = llenarlista(lista)
    print(burbuja(lista))