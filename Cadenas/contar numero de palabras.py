# Implementa una función que cuente el
# número de palabras en una cadena.

def contar(cad):
    copia = cad.split(' ')
    return len(copia)

if __name__=='__main__':
    cad = input('Ingresa una frase: ')
    print('La frase tiene', contar(cad), 'palabra(s) owo')