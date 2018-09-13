import math

def ehHipotenusa(c):
    a = 1

    while a <= c:
        b = 1
        while b <= c:
            if a ** 2 + b ** 2 == c ** 2:
                return True
                break
            b = b + 1
        a = a + 1
    return False


def soma_hipotenusas(x):
    soma = 0
    i = 1

    while i <= x:
        if ehHipotenusa(i):
            soma = soma + i
        i = i + 1

    return soma
