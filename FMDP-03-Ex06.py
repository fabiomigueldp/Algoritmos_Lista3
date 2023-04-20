'''6. Classifique o triângulo. Baseado nos comprimentos dos seus lados, um triângulo pode ser
classificado como equilátero (quando os três lados tem o mesmo tamanho), isósceles (quando
apenas dois lados são iguais) ou escaleno (quando os três lados são diferentes). Escreva um
programa Python que recebe do usuário os comprimentos dos 3 lados de um triângulo e exiba
uma mensagem informando qual é o tipo do triângulo.'''

# Solicita o comprimento dos lados do triângulo

lado1 = float(input("Insira o comprimento do primeiro lado do triângulo: "))
lado2 = float(input("Insira o comprimento do segundo lado do triângulo: "))
lado3 = float(input("Insira o comprimento do terceiro lado do triângulo: "))

# Verifica se os comprimentos são válidos

if lado1 > 0 and lado2 > 0 and lado3 > 0:
    # Verifica se forma um triângulo
    if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado3 + lado1 > lado2:
        # Verifica o tipo de triângulo
        if lado1 == lado2 and lado2 == lado3:
            tipo = "equilátero"
        elif lado1 == lado2 or lado2 == lado3 or lado3 == lado1:
            tipo = "isósceles"
        else:
            tipo = "escaleno"
        # Imprime a resposta
        print(f"O triângulo é {tipo}.")
    else:
        print("Os comprimentos informados não formam um triângulo.")
else:
    print("Os comprimentos informados não são válidos.")