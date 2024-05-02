# Dada una tupla de números, encuentra el
# número más grande y el más pequeño.
import random

def mayorymenor(tupla):
    nummayor = max(tupla)
    nummenor = min(tupla)
    return nummayor, nummenor

if __name__=='__main__':
    tupla = (random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100), random.randint(1, 100))
    print(tupla, mayorymenor(tupla))