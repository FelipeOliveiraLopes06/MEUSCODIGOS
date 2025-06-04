arquivo = open('intervalo.txt', 'w')  # Abre (ou cria) o arquivo 'intervalo.txt' para escrita
valor = input("Digite um valor: ")    # Solicita ao usuário que digite um valor
arquivo.write(valor)                  # Escreve o valor digitado no arquivo

valor = float(valor)                  # Converte o valor digitado para número decimal (float)

# Verifica em qual intervalo o valor se encaixa e exibe a mensagem correspondente
if 0 <= valor <= 25:
    print("Intervalo [0,25]")
elif 25 < valor <= 50:
    print("Intervalo (25,50]")
elif 50 < valor <= 75:
    print("Intervalo (50,75]")
elif 75 < valor <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")        # Se o valor estiver fora do intervalo 0-100

arquivo.close()                       # Fecha o arquivo

