#                     DESAFIO


# Fazendo a Tabuada de 1 a 10 

numero = int(input("Digite um número de 1 a 10 para ver a tabuada: "))

if 1 <= numero <= 10:
    print(f"\nTabuada do {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
else:
    print("ERROR \nDigite um número entre 1 e 10.")


# Criando um vetor vazio para armazenar os números
numeros = []

# Recebendo 10 números do usuário
for i in range(10):
    numero = int(input(f"Digite o {i+1}º número: "))
    numeros.append(numero)

# Inicializando variáveis para o maior número e sua posição
maior_valor = numeros[0]
posicao_maior = 0

# Percorrendo o vetor para encontrar o maior valor e sua posição
for i in range(1, len(numeros)):
    if numeros[i] > maior_valor:
        maior_valor = numeros[i]
        posicao_maior = i

# Exibindo o maior valor e sua posição
print(f"O maior valor é {maior_valor} e está na posição {posicao_maior}.")


