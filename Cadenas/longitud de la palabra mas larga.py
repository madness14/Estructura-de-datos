# Dada una cadena, encuentra la longitud
# de la palabra más larga.
def palabra(cad):
    cadenacomp = cad.split(' ')
    n = len(max(cadenacomp))
    return n

if __name__=='__main__':
    cad = input('Ingresa una o varias palabras owo: ')
    print('La palabra mas larga tiene', palabra(cad), 'caracteres')