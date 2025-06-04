# quadrado, retângulo, triângulo, losango, trapézio




def quadrado():
    lado = float(input("Digite o valor do lado do quadrado"))
    area = lado ** 2
    perimetro = 4 * lado
    


def retangulo():
    comprimento = float(input("Digite o valor do Comprimento"))
    altura = float(input("Digite o valor da Altura"))
    area = comprimento * altura
    perimetro = 2 * (comprimento, altura)
    return area, perimetro

def triangulo():
    base = float(input("Digite o valor da Base"))
    altura = float(input("Digite o valor da Altura"))
    lado1 = float(input("Digite o valor do lado A"))
    lado2 = float(input("Digite o valor do lado B"))
    area = (base * altura) /2
    perimetro = lado1 + lado2
    return area, perimetro

def losangulo():
    diagonal1 = float(input("Digite o valor da diagonal A"))
    diagonal2 = float(input("Digite o valor da diagonal B"))
    lado = float(input("Digite o valor do lado"))
    area = (diagonal1 * diagonal2) / 2
    perimetro = 4 * lado
    return area, perimetro

def trapezio():
    base_maior = float(input("Digite o valor da Base Menor"))
    base_menor = float(input("Digite o valor da Base Maior"))
    altura = float(input("Digite o valor da Altura"))
    lado1 = float(input("Digite o valor do lado A"))
    lado2 = float(input("Digite o valor do lado B"))
    area = ((base_maior + base_menor) * altura) / 2
    perimetro = base_maior + base_menor + lado1 + lado2
    return area, perimetro


quadrado()
retangulo()
triangulo()
losangulo()
trapezio()