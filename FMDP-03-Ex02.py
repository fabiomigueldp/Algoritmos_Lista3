'''2. Idade canina. É comum dizermos que um ano de um cachorro equivale a 7 anos de um
humano. Porém, essa conversão simples erra em não reconhecer que cachorros se tornam
adultos em cerca de 2 anos. Assim, algumas pessoas acreditam que é melhor contar os dois
primeiros anos como 10.5 anos caninos, e os anos restantes como 4 anos caninos cada.
Escreva um programa que implemente a conversão de anos cronológicos para anos caninos.
Certifique-se que seu programa funciona tanto para conversão de idades até 2 anos
cronológicos e também maiores que 2 anos cronológicos. Seu programa deve exibir uma
mensagem de erro se o usuário entrar com um número negativo.'''

# Solicita a idade humana

idadeHumano = int(input("Insira a idade humana: "))

# Limita o valor no intervalo 0<=idadeHumano

while True:
    if idadeHumano >= 0:
        break
    print("Valor inválido, tente novamente.")
    idadeHumano = int(input("Insira a idade humana: "))

# Cálculo

if idadeHumano <= 2:
    idadeCachorro = idadeHumano * 10.5
else:
    idadeCachorro = (idadeHumano - 2) * 4 + 21

# Imprime a resposta

print(f"Idade do cachorro: {idadeCachorro} anos.")