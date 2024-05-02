# Dada una cadena de palabras separadas
# por espacios, invierte el orden de
# las palabras.

def cadenamod(cad):
    cad = cad.split(' ')
    nuevacad = cad[::-1]
    return ' '.join(nuevacad)

if __name__=='__main__':
    cad = input('Ingresa una cadena con espacios owo: ')
    print(cadenamod(cad))