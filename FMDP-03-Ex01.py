'''1. Par ou ímpar. Escreva um programa Python que recebe do usuário um número inteiro. Seu
programa deve então exibir uma mensagem indicando se o número fornecido é par ou ímpar.'''

# Solicita os dados

n = int(input("Insira um número inteiro: "))

# Processa os dados

if n % 2 == 0:
    print("Seu número é par.")
else:
    print("seu número é impar.")

