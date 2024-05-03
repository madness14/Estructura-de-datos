# Dada una lista de elementos, regresar una nueva lista con los elementos repetidos eliminados
# La solución debe utilizar recursividad para que cuente
# Este es del profe xd

def eliminar_repetidos2(lista: list) -> list:
    """
    Elimina elementos repetidos de una lista
    """
    if not lista:
        return []
    frente = lista[0]
    resto = lista[1:]
    demas = eliminar_repetidos2(resto)
    if frente in demas:
        return demas
    else:
        return [frente] + demas


def eliminar_repetidos_rec(lista: list, acumulador: list) -> list:
    """
    Elimina los elementos de la lista de
    entrada de forma recursiva.

    lista: lista,
    acumulador: list, se debe inicializar como []
    returns: list 
    """
    if not lista:
        return acumulador
    frente = lista[0]
    resto = lista[1:]
    if frente in acumulador:
        return eliminar_repetidos_rec(resto, acumulador)
    else:
        acumulador.append(frente)
        return eliminar_repetidos_rec(resto, acumulador)

def eliminar_repetidos(lista: list) -> list:
    """
    Regresa una lista sin elementos repetidos.

    lista
    returns: list 
    """
    return eliminar_repetidos_rec(lista, [])

if __name__ == '__main__':
    n = int(input())
    lista = [input() for _ in range(n)]
    print(eliminar_repetidos(lista))
