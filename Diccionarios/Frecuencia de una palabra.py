def frec(l):
    d = {}
    for i in range(len(l)):
        n = l.count(l[i])
        d[l[i]]= n
    return d

def imp(d):
    for l, v in d.items():
        print('%s: %s' % (l, v))

if __name__=='__main__':
    cad = input()
    l = []
    l = cad.split(' ')
    l = sorted(l)
    d = frec(l)
    imp(d)