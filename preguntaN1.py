# 1. Implemente un algoritmo, usando una función recursiva, que resuelva la siguiente sumatoria:
# K(n, p) = p + 2 * p+3 * p + 4 * p + ... + n * p
n = int(input('Ingrese el valor de n: '))
p = int(input('Ingrese el valor de P: '))


def sumatoriaK(n, p):
    if n == 1:
        return p
    return n*p+sumatoriaK(n-1, p)


print('La sumatoria de K(n,p) = ', sumatoriaK(n, p))
