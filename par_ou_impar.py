import random  # Importa a biblioteca para gerar números aleatórios

def par_ou_impar():
    print("Bem-vindo ao jogo de Par ou Ímpar!")
    print("Você jogará contra o computador. Vamos começar!\n")

    opcoes = ["par", "impar"]  # Opções válidas para escolha do jogador
    pontos_jogador = 0  # Contador de pontos do jogador
    pontos_computador = 0  # Contador de pontos do computador
    rodadas = 3  # Número total de rodadas do jogo

    # Loop principal do jogo: 3 rodadas
    for rodada in range(1, rodadas + 1):
        print(f"Rodada {rodada} de {rodadas}")

        # Loop para garantir que o jogador escolha "par" ou "impar"
        while True:
            escolha_jogador = input("Escolha: Par ou Ímpar? ").lower()  # Converte para minúsculas
            if escolha_jogador in opcoes:
                break  # Saí do loop se a escolha for válida
            print("Escolha inválida! Digite 'Par' ou 'Ímpar'.\n")

        # Loop para garantir que o número digitado seja um inteiro de 0 a 10
        while True:
            try:
                numero_jogador = int(input("Escolha um número entre 0 e 10: "))
                if 0 <= numero_jogador <= 10:
                    break  # Número válido
                print("Número inválido! Escolha entre 0 e 10.\n")
            except ValueError:
                print("Entrada inválida! Digite um número inteiro.\n")

        numero_computador = random.randint(0, 10)  # Computador escolhe número aleatório
        print(f"O computador escolheu o número: {numero_computador}")

        soma = numero_jogador + numero_computador  # Soma dos dois números
        resultado = "par" if soma % 2 == 0 else "impar"  # Verifica se a soma é par ou ímpar
        print(f"A soma dos números é {soma}, que é {resultado}.")

        # Verifica quem ganhou a rodada
        if escolha_jogador == resultado:
            print("Você ganhou a rodada!\n")
            pontos_jogador += 1  # Adiciona ponto para o jogador
        else:
            print("O computador ganhou a rodada!\n")
            pontos_computador = pontos_computador + 1  # Adiciona ponto para o computador

    # Exibe o placar final após as rodadas
    print("Fim de jogo!")
    print(f"Placar final: Você {pontos_jogador} x {pontos_computador} Computador")

# Chamada da função para iniciar o jogo
par_ou_impar()
