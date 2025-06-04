# CHAMANDO UM TIME E ACESSANDO UM JOGADOR
time = ["Ronaldo", "Romario", "Neymar", "Pelé", "Ronaldinho"]
print (time)
print ("Camisa 9: " + time[0])
print ("Camisa 11: " + time[1])
print ("Camisa 7: " + time[2])
print ("Camisa 10: " + time[3])
print ("Camisa 80: " + time[4])

# ACESSANDO UM JOGADOR(DE TRAS PRA FRENTE)
print ("\nJogador: " + time[-1])
print ("Jogador: " + time[-2])
print ("Jogador: " + time[-3])
print ("Jogador: " + time[-4])
print ("Jogador: " + time[-5])

# SUBISTITUINDO UM JOGADOR
time[1] = "Yasmin"
print (time)

# ADICIONA UM JOGADOR
time = ["Ronaldo", "Romario", "Neymar", "Pelé", "Ronaldinho"]
time.append("Coutinho")
print (time)

# INSERE UM JOGADOR NA POSIÇÃO ONDE COLOCAR
time = ["Ronaldo", "Romario", "Neymar", "Pelé", "Ronaldinho"]
time.insert(0, "Felipe")
print (time)

# REMOVE UM JOGADOR
time = ["Ronaldo", "Romario", "Neymar", "Pelé", "Ronaldinho"]
JogadorRemovido = time.pop(2)
print (f"\nTREINADOR TIROU: {JogadorRemovido}\n")

# REMOVE O JOGADOR DE ACORDO COM O NOME QUE COLOCAR
time = ["Ronaldo", "Romario", "Neymar", "Pelé", "Ronaldinho"]
time.remove("Neymar")
print (time)
print ("Neymar SOFREU UMA LESÃO GRAVE E NÃO  VAI PARA O JOGO")

#MOSTRA O TEXTO EM ORDEM ALFABETICA
time = ["Ronaldo", "Romario", "Neymar", "Pelé", "Ronaldinho"]
time.sort()
print (time)

# MOSTRA O TEXTO EM ORDEM ALFABETICA(REVERSO)
time = ["Ronaldo", "Romario", "Neymar", "Pelé", "Ronaldinho"]
time.sort(reverse = True)
print (time)

# VARIAÇÃO DO -SORT-
time = ["Ronaldo", "Romario", "Neymar", "Pelé", "Ronaldinho"]
print (sorted (time))

# VARIAÇÃO DO -SORT- REVERSE TRUE
time = ["Ronaldo", "Romario", "Neymar", "Pelé", "Ronaldinho"]
print (sorted (time, reverse = True))

# INVERTE A ORDEM DA LISTA
time = ["Ronaldo", "Romario", "Neymar", "Pelé", "Ronaldinho"]
time.reverse()
print (time)
