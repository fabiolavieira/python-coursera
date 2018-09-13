n = -1
lista = []

while n != 0:
    n = int(input("Digite um número: "))
    if n != 0:
        lista.append(n)

tam = len(lista)

for x in lista[tam-1::-1]:
    print(x)
