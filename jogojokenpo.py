import random 

def pedra_papel_tesoura():
    print("Bem-vindo ao jogo de Pedra, Papel e Tesoura!")
    print("Você jogará contra o computador. Vamos começar!")

    opcoes = ["pedra", "papel", "tesoura"]
    pontos_jogador = 0
    pontos_computador = 0
    rodadas = 5

    for rodada in range(1, rodadas + 1):
        print(f"Rodada {rodada} de {rodadas}")

        while True:
            print("Escolha uma opção: Pedra, Papel ou Tesoura")
            escolha_jogador = input("Sua escolha: ").lower()

            if escolha_jogador in opcoes:
                break
            else:
                print("Escolha inválida. Tente novamente.\n")

        escolha_computador = random.choice(opcoes) 
        print(f"O Computador escolheu: {escolha_computador}")

        if escolha_computador == escolha_jogador:
            print("Empate!")
        elif (escolha_jogador == "pedra" and escolha_computador == "tesoura") or \
             (escolha_jogador == "papel" and escolha_computador == "pedra") or \
             (escolha_jogador == "tesoura" and escolha_computador == "papel"):
             print("Você ganhou!")
             pontos_jogador += 10
        else:
            print("O Computador ganhou!\n")
            pontos_computador += 10

    print("Fim de jogo")
    print(f"Placar final: Você {pontos_jogador} x {pontos_computador} Computador")

    if pontos_jogador > pontos_computador:
        print("Você ganhou!")
    elif pontos_jogador < pontos_computador:
        print("O computador ganhou!")
    else:
        print("O jogo terminou empatado!")

pedra_papel_tesoura()
