#Encuentra el número más grande en 
#una lista de números enteros.

def nummayor(n, lista):
    for i in range(n):
        lista.append(input())
    return max(lista)

if __name__=='__main__':
    n = int(input())
    lista = []
    print(nummayor(n, lista))