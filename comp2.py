import random

print("BEM VINDO AO JOGO!")
print("O COMPUTADOR VAI ESCOLHER UM NUMERO ENTRE 1 E 20.")
print("VOCÊ TEM 5 TENTATIVAS PARA ACERTAR. \n")

numero = random.randint (1,20)
tentativas = 5


for tentativa in range(1, tentativas + 1):
    print(f"TENTATIVA {tentativa} DE {tentativas}")

    while True:
        try:
            palpite = int(input("DIGITE O NUMERO ESCOLHIDO: "))
            if 1 <= palpite <= 20:
                break
            else:
                print("MEU DEUS, É PRA DIGITAR UM NUMERO ENTRE 1 E 20.")
        except ValueError:
            print("DEU ERRADO, DIGITE UM NUMERO INTEIRO")

    if palpite < numero:
        print("QUASE, TA BAIXO!\n")
    elif palpite > numero:
        print("QUASE, TA ALTO!\n")
    else:
        print(f"PARABENS ACERTOU O NUMERO {numero} NA  TENTATIVA {tentativa}!\n")
        break
else:
    print(f"Você perdeu! O número correto era {numero}.\n")

print("Fim de jogo!")