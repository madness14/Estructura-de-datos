# Dada una lista de números, encuentra
# todos los pares de números cuya suma
# sea igual a un número objetivo dado.

def llenarlista(n):
    lista = []
    for i in range(n):
        lista.append(int(input('Ingresa elemento %s: '% (i+1))))
    if not lista:
        print('feo unu')
        exit(1)
    else:
        return lista

def sumadeunnumero(lista, sum):
    paresqsuman = ''
    for i in range(len(lista)):
        for j in range(len(lista)):
            if lista[i]+lista[j]==sum:
                paresqsuman += '(' + str(lista[i]) + ',' + str(lista[j]) + ')'
    if not paresqsuman:
        return 'Ninguno encontrado :c'
    else:
        return paresqsuman

if __name__=='__main__':
    n = int(input('Ingresa el num de elementos feos de la lista owo (puros numeros): '))
    lista = llenarlista(n)
    sum = int(input('Ingresa un entero: '))
    print('Lista de pares que suman: ', sumadeunnumero(lista, sum))
    