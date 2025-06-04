# Quando usado parenteses é uma tupla, serve para listas que não podem ser alteradas.

time = ("Ronaldo", "Romario", "Neymar", "Pelé", "Ronaldinho")
print (time)
#time.append("Coutinho")


# Adicionando itens a um set
x = set()
x.add(19)
x.add(18)
x.add(10)
x.add(10)
print(x)


#Bolean | Os valores boleanos podem ser atribuidos por meio de expressão
a = True
b = False
c = 1 < 2
d = 7 > 12
e = None
print (a,b,c,d,e)


#Dicionario | Criado com {} que significa uma chave e um  valor 
dicionario = {"chave1" : "valor1", "chave2" :"valor2"}
print(dicionario["chave2"])

#Tradutor |  Criado com {} que significa uma chave e um  valor
Tradutor = {"Mouse" : "Rato" , "Dog" : "Cachorro" , "Cat" : "Gato"}
print(Tradutor["Dog"])


#2 Dicionario | podemos chamar itens de uma lista presente na posição referente a chave
dicionario2 = {"key1" : 123, "Key2" : [12,23,33], "Key3":["item0", "item1" "item2"] }
dicionario2 ["Key3"] [0]

#3 Dicionario | criado com  atribuições
#dict_ seguido do método usado, por exemplo dict_keys() e dict_values().
D = {}
D["yas"] = "mulher"
D["lipe"] = "homem"
print(D)
print(D.keys())
print(D.values())
print(D.items())



