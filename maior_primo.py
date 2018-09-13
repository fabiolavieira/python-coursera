def primo(n):
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


def maior_primo(x):
    ehprimo = False

    while ehprimo == False:
        ehprimo = primo(x)
        x = x - 1

    return x + 1
