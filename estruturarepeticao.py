
#FOR

#imprimindo numeros em uma lista
números = [1,2,3,4,5,6,7,8,9,10]
for num in números:
 print(num)

 #imprimindo numeros em um alcance:1 a 10
for num1 in range(1,11):
 print(num1)

#imprimindo apenas numeros pares de 1 a 10
 for num1 in range(1,11):
  if (num1 %2 ==0):
    print (f"PAR: {num1}")
  else:
    print(f"IMPAR: {num1}")


#imprimindo as letras de uma string
for letra in "futebol":
 print (letra)


#WHILE

# Somando todos os números de 1 a 1000 enquanto a soma é menor que 100

soma = 0
numeros = range(1,1000)
i= 0
while soma < 50:
 soma += numeros[i]
 i+=1
 print(soma)


# # Este código usa um laço while para contar de 0 até 4.
# A cada repetição, ele imprime o valor atual de x e uma mensagem indicando que x ainda é menor que 5.
# Depois, x é incrementado em 1.
# Quando x atinge 5, a condição do while se torna falsa e o bloco else é executado, imprimindo "FIM!".
x = 0
while x < 5:
 print("valor de x:", x)
 print("x ainda é menor que 5, vamos somar 1")
 x += 1
else:
 print("FIM!")

































































