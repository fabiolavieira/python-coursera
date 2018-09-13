def remove_repetidos(lista):
    lista.sort()
    nova = []

    for i in lista:
        if i not in nova:
            nova.append(i)
    return nova
