n = int(input("Digite um número inteiro: "))

count = 0
i = 1

while i <= n:
    if n%i == 0:
        count = count + 1
    i = i + 1

if count == 2:
    print("primo")
else:
    print("não primo")
