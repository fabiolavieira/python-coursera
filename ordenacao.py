import math

x1 = int(input("Digite o valor da coordenada x: "))
y1 = int(input("Digite o valor da coordenada y: "))
x2 = int(input("Digite o valor da coordenada x: "))
y2 = int(input("Digite o valor da coordenada y: "))

d = sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

if d >= 10:
    print("longe")
else:
    print("perto")
    
