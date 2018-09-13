import math

a = int(input("Digite o parâmetro a: "))
b = int(input("Digite o parâmetro b: "))
c = int(input("Digite o parâmetro c: "))

delta = (b ** 2) - 4 * a * c

if delta < 0:
    print("esta equação não possui raízes reais")
elif delta == 0:
    print("a raiz desta equação é", -b/2*a)
else:
    raiz = math.sqrt(delta)
    x = (-b + raiz)/2*a
    y = (-b - raiz)/2*a
    if x < y:
        print("as raízes da equação são", x, "e", y)
    else:
        print("as raízes da equação são", y, "e", x)
