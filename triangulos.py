import math  # Importa a biblioteca math para usar a função de raiz quadrada

def pode_ser_triangulo(a, b, c):
    # Verifica se três lados podem formar um triângulo (regra da desigualdade triangular)
    return a + b > c and a + c > b and b + c > a

def tipo_triangulo(a, b, c):
    # Determina o tipo de triângulo com base nos lados
    if a == b == c:
        return "Equilátero"  # Todos os lados iguais
    elif a == b or b == c or c == a:
        return "Isósceles"  # Dois lados iguais
    else:
        return "Escaleno"  # Todos os lados diferentes

def area_triangulo(a, b, c):
    # Calcula a área do triângulo usando a fórmula de Heron
    s = (a + b + c) / 2  # Calcula o semi-perímetro
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))  # Fórmula de Heron
    return area

# Solicita os lados do triângulo ao usuário (como números com ponto decimal)
a = float(input("digite o primeiro lado do triangulo:")) 
b = float(input("digite o segundo lado do triangulo:"))
c = float(input("digite o terceiro lado do triangulo:"))

# Verifica se os valores podem formar um triângulo
if pode_ser_triangulo(a, b, c):
    # Se sim, imprime o tipo de triângulo e sua área
    print(f"Os lados {a}, {b} e {c} formam um triangulo {tipo_triangulo(a, b, c)}.")
    print(f"A area do triangulo é {area_triangulo(a, b, c):.2f} unidades quadradas.")
else:
    # Caso contrário, informa que não formam um triângulo
    print("Os valores fornecidos não formam um triangulo.")

# Essas duas chamadas estão aqui, mas não fazem nada visível:
tipo_triangulo(a, b, c)  # Sem efeito, pois o valor não é usado nem impresso
area_triangulo(a, b, c)  # Sem efeito, pois o valor não é usado nem impresso








    