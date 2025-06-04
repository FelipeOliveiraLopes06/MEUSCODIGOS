# Define a função com país como parâmetro
def cidadeEPais(cidade, pais="Brasil"):
    print(f"{cidade} está localizada dentro {pais}.")

# Chamadas da função com diferentes cidades
cidadeEPais("São Paulo")              
cidadeEPais("Paris", pais="França") #mesma coisa que ("Paris", "França")
cidadeEPais("Varzea Paulista") 
