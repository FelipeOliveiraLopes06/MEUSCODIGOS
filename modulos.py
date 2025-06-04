import math  # Importa o módulo math para usar funções matemáticas
import os  # Importa o módulo os para interagir com o sistema operacional
from mode import calculo as hj

# Verifica se o arquivo "arquivo.txt" existe
if os.path.exists("arquivo.txt"):
    os.remove("arquivo.txt")  # Se existir, remove o arquivo
else:
    print("O arquivo não exixte")  # Caso não exista, exibe uma mensagem


print(dir(math))  # Mostra todos os atributos e funções disponíveis no módulo math
help(math.log)  # Mostra a documentação da função math.log (logaritmo)

print(dir(os))  # Mostra todos os atributos e funções disponíveis no módulo os
help(os.renames)  # Mostra a documentação da função os.renames (renomeia diretórios)




