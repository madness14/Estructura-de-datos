# Dada una lista de tuplas (nombre, edad),
# ordena la lista por edades.

def ordenar(lista):
    listaord = sorted(lista, key =lambda x: x[1])            
    return listaord

if __name__=='__main__':
    lista = [('Ander', 18), ('Danna',  20), ('Ian', 17), ('Cris', 25), ('Montane', 19)]
    print(ordenar(lista))