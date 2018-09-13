x = int(input("Digite um número inteiro: "))
count = 0
dig = -1
while x > 0:
    n = x % 10
    if n == dig:
        count = count + 1
    dig = n
    x = x // 10

if count == 0:
    print("nao")
else:
    print("sim")
