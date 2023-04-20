'''9. Data de feriado. A tabela abaixo mostra os feriados nacionais brasileiros que caem sempre no
mesmo dia (em oposição aos feriados variáveis como carnaval e corpus christi).
Feriado Data
Confraternização universal 1o. de janeiro
Tiradentes 21 de abril
Dia do trabalho 1o. de maio
Independência do Brasil 7 de setembro
Nossa Senhora Aparecida 12 de outubro
Finados 2 de novembro
Proclamação da República 15 de novembro
Natal 25 de dezembro
Escreva um programa Python que leia do usuário o mês e o dia de uma determinada data. Se
o mês e o dia corresponderem a uma das datas da tabela acima, seu programa deve exibir o
nome do feriado. Caso contrário o programa deve informar que o dia e o mês informados não
correspondem a um feriado nacional.'''

# Solicita o mês e o dia da data

mes = int(input("Insira o mês (1 a 12): "))
dia = int(input("Insira o dia (de 1 a 31): "))

# Limita o valor no intervalo

while True:
    if mes >= 1 and mes <= 12 and dia >= 1 and dia <= 31:
        break
    print("Valor inválido, tente novamente.")
    mes = int(input("Insira o mês (1 a 12): "))
    dia = int(input("Insira o dia (de 1 a 31): "))

# Verifica se a data corresponde a um feriado
if mes == 1 and dia == 1:
    feriado = "Confraternização universal"
elif mes == 4 and dia == 21:
    feriado = "Tiradentes"
elif mes == 5 and dia == 1:
    feriado = "Dia do trabalho"
elif mes == 9 and dia == 7:
    feriado = "Independência do Brasil"
elif mes == 10 and dia == 12:
    feriado = "Nossa Senhora Aparecida"
elif mes == 11 and dia == 2:
    feriado = "Finados"
elif mes == 11 and dia == 15:
    feriado = "Proclamação da República"
elif mes == 12 and dia == 25:
    feriado = "Natal"
else:
    feriado = "nenhum"

# Imprime a resposta

if feriado != "nenhum":
    print(f"A data informada corresponde ao feriado nacional de {feriado}.")
else:
    print("A data informada não corresponde a um feriado nacional.")