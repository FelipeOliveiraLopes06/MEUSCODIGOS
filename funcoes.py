#definindo uma simples função.

def boas_vindas ():
    print("Agora é 8:50")

boas_vindas()

#definindo uma simples função com o nome do usuario.
def boas_vindas (nomeDeUsuario):
    print("Bem vindo(a)", nomeDeUsuario, "ao Corinthians"   )

boas_vindas("Felipe")

#A função calcular_velocidade recebe distância e tempo, calcula a velocidade média e imprime o resultado.
def velocidade(distancia, tempo):
    print(distancia/tempo)
velocidade(100, 5)

def menor(a,b):
    
    if a<=b:
        return a
    else:
        return b

a = 20
b= 10
print("O valor entre ", a, "e", b, "é", menor(a,b))






