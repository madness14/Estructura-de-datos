# Crea una tupla de tuplas a partir de
# una lista de listas.

def tupladetuplas(listadelistas):
    for i in range(len(listadelistas)):
        listadelistas[i] = tuple(listadelistas[i])
    tupladetuplas = tuple(listadelistas)
    return tupladetuplas

if __name__=='__main__':
    listadelistas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(tupladetuplas(listadelistas))