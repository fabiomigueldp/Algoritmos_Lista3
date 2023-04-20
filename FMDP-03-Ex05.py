'''5. Nome do mês e número de dias. A quantidade de dias de um mês pode variar de 28 a 31
dias. Neste exercício você deve criar um programa Python que recebe do usuário o nome de
um mês (como uma string). Então seu programa deve exibir uma mensagem informando a
quantidade de dias daquele mês. Caso o mês seja fevereiro, sua mensagem pode informar
“28 ou 29 dias”.'''

# Solicita o nome do mês

mes = input("Insira o nome de um mês: ")

# Verifica qual o número de dias do mês

if mes == "Janeiro" or mes == "Março" or mes == "Maio" or mes == "Julho" or mes == "Agosto" or mes == "Outubro" or mes == "Dezembro":
    dias = 31
elif mes == "Abril" or mes == "Junho" or mes == "Setembro" or mes == "Novembro":
    dias = 30
elif mes == "Fevereiro":
    dias = "28 ou 29"
else:
    print("Valor inválido, tente novamente.")

# Imprime a resposta

if dias != None:
    print(f"O mês de {mes} tem {dias} dias.")