# Cuenta el número de veces que aparece
# una letra específica en una cadena.
cad = input('Escribe algo: ')
n = input('Ingresa la letra a buscar: ')
cont = 0
for i in range(len(cad)):
    if n==cad[i]:
        cont += 1
print('Aparece ', cont, ' veces')

#Tambien...
cad = input("Escribe algom: ")
letra = input("Ingresa la letra a buscar: ")
cont = cad.count(letra)
print('Aparece ', cont,' veces owo')
