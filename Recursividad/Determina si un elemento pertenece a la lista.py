# Crea una solución recursiva para determinar is un elemento x pertenece a una lista
# Nota: para que la actividad cuente, la solución debe ser recursiva

def llenarlista(n):
    if n == 0:
        return l
    l.append(int(input()))
    return llenarlista(n-1)

def rec(l, n, x):
    if not l:
        return False
    if n == 0:
        if l[n] == x:
            return True
        else:
            return False
    if l[n] == x:
        return True
    return rec(l, n-1, x)

if __name__=='__main__':
    l = []
    x = int(input())
    n = int(input())
    l = llenarlista(n)
    n = n - 1
    print(rec(l, n, x))