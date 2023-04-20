'''7. Níveis de barulho. A tabela abaixo mostra uma lista de volume sonoro em decibéis para
diferentes tipos comuns de barulhos.
Barulho Nivel de decibéis (dB)
Britadeira 130
Cortador de grama 106
Despertador 70
Sala silenciosa 40
Escreva um programa Python que receba do usuário um nível de volume em decibéis. Se o
usuário entrar com um valor igual a um daqueles listados na tabela, então seu programa deve
exibir uma mensagem informando o tipo de barulho da tabela equivalente ao valor informado.
Se o usuário entrar um valor intermediário entre dois valores da tabela, então seu programa
deve exibir uma mensagem informando que o nível está entre os dois barulhos (deve informar
quais são eles). Certifique-se também que seu programa exiba mensagens apropriadas caso o
usuário entre com valor menor que o menor valor da tabela ou maior que o maior valor.
'''

# Solicita o valor de decibéis 

dB = int(input("Insira o nível de volume em decibéis: "))

# Verifica o valor informado

if dB < 40:
    print("Esse decibéis está abaixo do nível de volume de uma sala silenciosa.")
elif dB == 40:
    print("Esse decibéis corresponde ao nível de volume de uma sala silenciosa.")
elif dB > 40 and dB < 70:
    print("Esse decibéis está entre o nível de volume de uma sala silenciosa e de um despertador.")
elif dB == 70:
    print("Esse decibéis corresponde ao nível de volume de um despertador.")
elif dB > 70 and dB < 106:
    print("Esse decibéis está entre o nível de volume de um despertador e de um cortador de grama.")
elif dB == 106:
    print("Esse decibéis corresponde ao nível de volume de um cortador de grama.")
elif dB > 106 and dB < 130:
    print("Esse decibéis está entre o nível de volume de um cortador de grama e de uma britadeira.")
elif dB == 130:
    print("Esse decibéis corresponde ao nível de volume de uma britadeira.")
elif dB > 130:
    print("Esse decibéis está acima do nível de volume de uma britadeira.")