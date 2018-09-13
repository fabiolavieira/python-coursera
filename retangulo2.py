largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))

larg = 1
alt = 1

while alt <= altura:
    if alt == 1 or alt == altura:
        larg = 1
        while larg <= largura:
            print("#", end="")
            larg = larg + 1
    else:
        aux = 1
        print("#", end="")
        while aux <= largura - 2:
            print(" ", end="")
            aux = aux + 1
        print("#", end="")
    print()
    alt = alt + 1

