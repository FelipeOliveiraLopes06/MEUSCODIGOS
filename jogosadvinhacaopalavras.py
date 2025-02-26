## importa uma biblioteca para usarmos
import random

## funcao
def jogo_advinhacao():
    print("Bem vindo ao Jogo de Adivinhacao de Palavras")
    print("Você receberá dicas para adivinhar a palavra secreta")

    ## dicionario
    palavras_e_dicas = {
    "gol": "Ação de marcar um ponto no jogo, quando a bola entra completamente na rede adversária.",
    "drible": "Movimento feito por um jogador para passar por um adversário com a bola.",
    "pênalti": "Tiro direto, geralmente marcado em situações de falta dentro da área, com o goleiro defendendo o chute.",
    "escanteio": "Quando a bola sai pela linha de fundo, tocada por um jogador da equipe adversária, sendo cobrada a partir do canto do campo.",
    "zagueiro": "Jogador responsável por defender a área e impedir que o time adversário marque gols.",
    "meia": "Jogador que atua no meio de campo, organizando as jogadas ofensivas.",
    "goleiro": "Jogador que tem a função de defender o gol e evitar que a bola entre na rede.",
    "falta": "Infração cometida por um jogador ao infringir as regras do jogo, resultando em uma cobrança ou cartão, dependendo da gravidade.",
    "cartão amarelo": "Advertência dada ao jogador por uma conduta antidesportiva. Se um jogador receber dois cartões amarelos, será expulso.",
    "cartão vermelho": "Expulsão de um jogador após uma infração grave ou acúmulo de advertências (dois cartões amarelos)."
    }
    
    ## para escolher palavra aleatoria, numero de tentativas
    palavra_secreta, dica=random.choice(list(palavras_e_dicas.items()))
    tentativas_restantes = 5
    
    ## condicao, se for verdadeiro e executado
    while tentativas_restantes > 0:
        print(f"Dica {dica}")
        print(f"Tentativas Restantes:{tentativas_restantes}")
        resposta = input("Qual é a palavra secreta?").lower()
        
        if resposta == palavra_secreta:
            print("\n Parabens, você acertou", palavra_secreta)
            break
        else:
            tentativas_restantes -= 1
            print("Palavra errada! tente novamente")
    if tentativas_restantes == 0:
        print("Você perdeu, a palavra era:", palavra_secreta)

jogo_advinhacao()