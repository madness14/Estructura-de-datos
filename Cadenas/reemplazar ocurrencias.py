# Reemplaza todas las ocurrencias de una
# subcadena en una cadena con otra subcadena.

def reemplazar(cad, ocurr, reemplazar):
    buscar = cad.replace(ocurr, reemp)
    if not buscar:
        return 'Ninguna ocurrencia encontrada :c'
    return buscar  
    
if __name__=='__main__':
    cad = input('Ingresa una cadena owwo:')
    ocurr = input('Ingresa la ocurrencia a buscar: ')
    reemp = input('Ingresa la cadena a reemplazar: ')
    print(reemplazar(cad, ocurr, reemp))