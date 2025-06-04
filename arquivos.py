# Cria ou sobrescreve o arquivo e escreve duas linhas
arquivo = open('teste.txt', 'w', encoding="utf-8")
arquivo.write("Este é um arquivo criado em Python!\n")  # Primeira linha com quebra de linha
arquivo.write("Segundo linha do conteúdo.")             # Segunda linha sem quebra
arquivo.close()  # Fecha o arquivo

# Abre o arquivo em modo de adição (append) e escreve mais uma linha
with open("teste.txt", "a") as arquivo:
    arquivo.write("\n slk num compensa")  # Adiciona uma nova linha ao final

# Abre o arquivo em modo de leitura e lê todo o conteúdo
with open('teste.txt', 'r') as arquivo:
    conteudo = arquivo.read()  # Lê todo o conteúdo do arquivo
    print(conteudo)  # Exibe o conteúdo lido

    conteudo2 = arquivo.read()  # Tenta ler de novo, mas já está no final -> retorna ''
    print(conteudo2)  # Imprime string vazia

    conteudo3 = arquivo.readline()  # Ainda no final do arquivo -> retorna ''
    print(conteudo3)  # Imprime string vazia

    arquivo.seek(0)  # Volta o ponteiro de leitura para o início do arquivo

    conteudo4 = arquivo.readlines()  # Lê todas as linhas e retorna uma lista
    print(conteudo4)  # Imprime a lista de linhas
