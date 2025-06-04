    #COMPETIÇÃO 1

r = input("ESCREVA UMA FRASE PARA SABER A QUANTIDADE DE VOGAIS:  ")
r.lower()
v = ("a","e","i","o","u") 
contagem = 0
contagemI = {"a":0,"e":0,"i":0,"o":0,"u":0}
for c in r:
    if c in v:
        contagem += 1
        contagemI [c] += 1





print(f"Quantidade de cada vogal{contagemI}")
print(f"Quantidade de Vogais: {contagem}")
    
      





   






 
