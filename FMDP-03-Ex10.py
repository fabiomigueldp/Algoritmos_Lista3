'''10. Cor da casa do tabuleiro. As posições das casas em tabuleiros de xadrez são identificadas
por uma letra e um número. A letra identifica a coluna e o número define a linha, conforme a
figura abaixo:
1
2
3
4
5
6
7
8
 hgfedcba
Escreva um programa Python que receba do usuário um posição. Use um comando if para
determinar se a coluna informada começa com quadrado preto ou branco. Então, use
aritmética de inteiros para determinar a cor do quadrado da linha correspondente. Por
exemplo, se o usuário entrou com o valor a1, então seu programa deve informar que o
quadrado é preto. Se o usuário entrou com o valor d5, então seu programa deve informar que
o quadrado é branco. Seu programa pode assumir que o usuário vai entrar valores válidos,
não sendo necessário verificar eventuais erros de input.'''

# Solicita a posição

posicao = input("Insira a posição do tabuleiro: ")

# Separa a posição

letra = posicao[0]
numero = int(posicao[1])

# Verifica se a coluna começa em preto ou branco

if letra in "aceg":
    cor = "branco"
elif letra in "bdfh":
    cor = "preto"

# Verifica a linha

if numero % 2 != 0:
    cor = "branco" if cor == "preto" else "preto"

# Imprime a resposta

print(f"O quadrado correspondente a posição {posicao} é {cor}.")