def computador_escolhe_jogada(n, m):
    max = m
    while (n - m) % (max+1) != 0 and (n - m) % (max+1) > 0:
        m = m - 1

    if m == 0:
        m = max
    return m


def usuario_escolhe_jogada(n, m):
    p = -1
    while p <= 0:
        p = int(input("Quantas peças você vai tirar? "))
        if p > m or p > n or p < 0:
            print("Oops! Jogada inválida! Tente de novo.")
            print()
            p = -1

    return p    


def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))

    p = 0
    usuario_joga = False
    vencedor = True
    
    if n%(m+1) == 0:
        usuario_joga = True
        print("Você começa")
    else:
        usuario_joga = False
        print("Computador começa")
    print()
    
    while n > 0:
        if usuario_joga == True:
            p = usuario_escolhe_jogada(n, m)

            if p > 1:
                print("Você tirou", p, "peças.")
            else:
                print("Você tirou uma peça.")
            
            n = n - p
            
            if n > 1:
                print("Agora restam", n, "peças no tabuleiro.")
            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")

            print()    
            usuario_joga = False
            
        else:
            p = computador_escolhe_jogada(n, m)
            
            if p > 1:
                print("O computador tirou", p, "peças.")
            else:
                print("O computador tirou uma peça.")
            
            n = n - p
            
            if n > 1:
                print("Agora restam", n, "peças no tabuleiro.")
            if n == 1:
                print("Agora resta apenas uma peça no tabuleiro.")

            print()    
            usuario_joga = True

    if usuario_joga == True:
        print("Fim do jogo! O computador ganhou!")
        vencedor = True
    else:
        print("Fim do jogo! Você ganhou!")
        vencedor = False
        
    return vencedor
    

def campeonato():
    jogo = 1
    res = False
    comp = 0
    user = 0
    
    while jogo <= 3:
        print("**** Rodada", jogo," ****")
        res = partida()

        if res == True:
            comp = comp + 1
        else:
            user = user + 1

        jogo = jogo + 1

    print("**** Final do campeonato! ****")
    print()
    print("Placar: Você", user, "X", comp, "Computador")



print("Bem-vindo ao jogo do NIM!")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")
escolha = int(input("Escolha: "))

if escolha == 1:
    print("Você escolheu uma partida!")
    partida()
elif escolha == 2:
    print("Você escolheu um campeonato!")
    campeonato()
else:
    print("Escolha inválida.")
print()
