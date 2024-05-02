# Dada una cadena, verifica si es un
# palíndromo.
def palindromo(pal):
    copia = pal[::-1]
    if not pal:
        return None
    if copia == pal:
        return True
    else:
        return False
    
if __name__=='__main__':
    pal = input('Ingresa la palabra a verificar owo: ')
    print('La palabra es palindromo: ', palindromo(pal))
    