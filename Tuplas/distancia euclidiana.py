# Implementa una función que reciba una
# tupla de coordenadas (x, y) y devuelva
# la distancia euclidiana desde el
# origen (0, 0).
def llenarlistadevolvertupla(lista):
    for i in range(2):
        lista.append(float(input('Ingresa la coordenada %s: '% (i+1))))
    return tuple(lista)

def distancia(tupla):
    #(A, B) = (tupla[0], tupla[1])
    return ((tupla[0])**2 + (tupla[1])**2)**(1/2)
    
# q tiene que ver la tupla? no se
# siendo sincero, me imagino que
# para editarlo desde el editor de
# texto per bah, ya quedo

if __name__=='__main__':
    lista = []
    tupla = llenarlistadevolvertupla(lista)
    print('La distancia euclidiana desde el origen (0, 0) es: ', distancia(tupla))
    