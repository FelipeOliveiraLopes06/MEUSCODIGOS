# Define a função prepara_acai que aceita vários ingredientes e um tamanho opcional (padrão é "Grande")
def prepara_acai(*ingredientes, tamanho="Grande"):
    # Imprime a mensagem inicial com o tamanho do açaí
    print("\nPreparando um Açaí", tamanho, end ="")
    
# Se houver ingredientes, imprime normalmente
    if ingredientes:
        print(" com os seguintes ingredientes:")
        for ingrediente in ingredientes:
            print("-", ingrediente)
    else:
        # Se não houver ingredientes, apenas pula linha
        print(" (sem ingredientes informados).")


# Chama a função com dois ingredientes e tamanho padrão ("Grande")
prepara_acai("banana", "granola")

# Chama a função com três ingredientes e tamanho especificado como "Grande"
prepara_acai("morango", "kiwi", "leite em pó", tamanho="Grande")

# Chama a função com um ingrediente e tamanho "pequeno"
prepara_acai("banana", tamanho="pequeno")

# Chama a função sem ingredientes, apenas com o tamanho padrão
prepara_acai()


#MESMO CODIGO SEM IMPRIMIR A ULTIMA LINHA DO "prepare_acai()"



# Define a função prepara_acai que aceita vários ingredientes e um tamanho opcional (padrão é "Grande")
def prepara_acai(*ingredientes, tamanho="Grande"):
    # Se não houver ingredientes, a função é encerrada sem imprimir nada
    if not ingredientes:
        return

    # Imprime a mensagem inicial com o tamanho do açaí
    print("\nPreparando um Açaí", tamanho, end="")

    # Imprime os ingredientes
    print(" com os seguintes ingredientes:")
    for ingrediente in ingredientes:
        print("-", ingrediente)


# Chama a função com dois ingredientes e tamanho padrão ("Grande")
prepara_acai("banana", "granola")

# Chama a função com três ingredientes e tamanho especificado como "Grande"
prepara_acai("morango", "kiwi", "leite em pó", tamanho="Grande")

# Chama a função com um ingrediente e tamanho "pequeno"
prepara_acai("banana", tamanho="pequeno")

# Chama a função sem ingredientes – agora não imprime nada
prepara_acai()


print("       \n \t   AGUARDANDO PEDIDOS.")





















import random

print("Bem-vindo ao jogo de Adivinhação!")
print("O computador escolheu um número entre 1 e 20.")
print("Você tem 5 tentativas para adivinhar.\n")

numero_secreto = random.randint(1, 20)
tentativas = 5

for tentativa in range(1, tentativas + 1):
    print(f"Tentativa {tentativa} de {tentativas}")

    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
            if 1 <= palpite <= 20:
                break
            else:
                print("Por favor, digite um número entre 1 e 20.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

    if palpite < numero_secreto:
        print("Muito baixo!\n")
    elif palpite > numero_secreto:
        print("Muito alto!\n")
    else:
        print(f"Parabéns! Você acertou o número {numero_secreto} na tentativa {tentativa}!\n")
        break
else:
    print(f"Você perdeu! O número correto era {numero_secreto}.\n")

print("Fim de jogo!")
