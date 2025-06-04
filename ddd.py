ddds = {
    "11": "São Paulo", 
    "71": "Bahia", 
    "65": "Mato Grosso",
    "21": "Rio de Janeiro",
    "41": "Paraná",
    "27": "Espirito Santo",
    "81": "Pernambuco"
}

ddd = input("Digite um DDD para saber o estado: ")

if ddd in ddds:
    print(f"O estado correspondente ao DDD {ddd} é {ddds[ddd]}.")
else:
    print("DDD não encontrado.")
