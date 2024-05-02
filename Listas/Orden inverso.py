#Crea una lista con números del 1 al 10 
# y luego imprime los elementos en orden 
# inverso.

def llenarlista(lista):
    for i in range(1, 11):
        lista.append(i)
    lista.reverse()
    return lista
if __name__=='__main__':
    lista = []
    print(llenarlista(lista))