# Dada una tupla de números, encuentra
# todas las combinaciones posibles de
# pares de elementos.

def combinaciones(tupla):
    comb = ''
    for i in range(len(tupla)):
        for j in range(len(tupla)):
            comb += '(' + str(tupla[i]) + ', ' + str(tupla[j])+ ')'     
    return comb
if __name__=='__main__':
    tupla = (1, 2, 3, 4)
    print(combinaciones(tupla))