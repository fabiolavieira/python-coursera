def ehPrimo(n):
    count = 0
    i = 1

    while i <= n:
        if n%i == 0:
            count = count + 1
        i = i + 1

    if count == 2:
        return True
    else:
        return False


def n_primos(n):
    count = 0
    i = 2
    
    while i <= n:
        if ehPrimo(i):
            count = count + 1
        i = i + 1
        
    return count
    
