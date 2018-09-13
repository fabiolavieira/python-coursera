largura = int(input("Digite a largura: "))
altura = int(input("Digite a altura: "))
larg = 0
alt = 0

while alt < altura:
    larg = 0
    while larg < largura:
        print("#", end="")
        larg = larg + 1
    print()
    alt = alt + 1
