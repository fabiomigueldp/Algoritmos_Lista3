'''4. Polígono regular. Crie um programa Python que determina e exibe o nome de um polígono
regular sendo fornecida pelo usuário a quantidade de lados. Seu programa deve suportar
polígonos de 3 a 10 lados (inclusive). Caso o usuário forneça valores fora desta faixa, o
programa deve exibir uma mensagem de erro.'''

# Solicita a quantidade de lados

lados = int(input("Insira a quantidade de lados do polígono: "))

# Limita o valor no intervalo 3<=valor<=10

while True:
    if lados >= 3 and lados <= 10:
        break
    print("Valor inválido, tente novamente.")
    lados = int(input("Insira a quantidade de lados do polígono: "))

# Verifica o formato do polígono

if lados == 3:
    nomePoligono = "Triângulo"
elif lados == 4:
    nomePoligono = "Quadrado"
elif lados == 5:
    nomePoligono = "Pentágono"
elif lados == 6:
    nomePoligono = "Hexágono"
elif lados == 7:
    nomePoligono = "Heptágono"
elif lados == 8:
    nomePoligono = "Octógono"
elif lados == 9:
    nomePoligono = "Eneágono"
elif lados == 10:
    nomePoligono = "Decágono"

# Imprime a resposta

print(f"O polígono é um {nomePoligono}.")