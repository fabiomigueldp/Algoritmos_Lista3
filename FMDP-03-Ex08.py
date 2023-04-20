'''8. Nota para frequência. Existem algumas diferenças entre as escolas latina e anglo-saxônica
de música. A mais conhecida é a diferença no nome das notas musicais. Na escola latina
temos Dó, Ré, Mi, Fá, Sol, Lá e Si. Os nomes correspondentes na escola anglo-saxônica são
C, D, E, F, G, A e B (do dó ao si, respectivamente. Além disso, a tecnologia MIDI incorporou
um número ao nome de cada nota indicando em qual oitava ela pertence. Por exemplo, o dó
central do piano é chamado de C4, o dó mais agudo, uma oitava acima é chamado de C5, e o
dó uma oitava abaixo (mais grave) é chamado de C3.
A tabela abaixo exibe as frequências de cada nota da oitava central do piano (cada nota
musical tem uma frequência específica em hertz).
Nota Frequência (Hz)
C4 261.63
D4 293.66
E4 329.63
F4 349.23
G4 392.00
A4 440.00
B4 493.88
Comece escrevendo um programa Python que recebe do usuário o nome de uma nota e exibe
a frequência correspondente. Seu programa deve aceitar todas as notas da tabela acima. Uma
vez que seu programa esteja funcionando, você deve modificá-lo para suportar todas as notas
de C0 a C8. Embora isso possa ser feito incluindo um monte de condições de ifs, elifs e else,
mas isso é extremamente "tosco" e deselegante, e portanto inaceitável como solução deste
exercício. Ao invés disso, você pode explorar as relações entre notas em oitavas adjacentes
(por exemplo relação da nota G4 com a nota G5, são duas notas sol, em oitavas diferentes).
Em particular, a frequência de uma nota em uma oitava é metade do valor da frequência da
mesma nota uma oitava acima. Por exemplo: se A4 tem 440.00Hz, a nota A5 tem 880.00Hz de
frequência e a nota A3 tem 220.00Hz. Tendo em mente estas relações, você consegue
resolver o problema para todas as notas musicais adicionais sem incluir novos casos nos seus
comandos condicionais.
Dicas: para resolver este exercício você terá que extrair caracteres individuais dos nomes
das notas com dois caracteres. Desta forma você consegue lidar separadamente com o
caractere da nota e o caractere da oitava. Depois que você tiver separado as partes,
obtenha a frequência da nota da oitava 4 usando os dados da tabela. Então, divida a
frequência por , onde x é o número da oitava fornecido pelo usuário no nome da nota.
Isto vai dobrar ou reduzir à metade corretamente as frequências em função da oitava.'''

# Solicita o nome da nota

nota = input("Insira o nome da nota musical: ")

# Separa a nota da oitava
nota_musical = nota[0]

# Limita o valor no intervalo
while True:
    if nota_musical == "C" or nota_musical == "D" or nota_musical == "E" or nota_musical == "F" or nota_musical == "G" or nota_musical == "A" or nota_musical == "B":
        break
    print("Valor inválido, tente novamente.")
    nota = input("Insira o nome da nota musical: ")
    nota_musical = nota[0]

# Separa a oitava
if len(nota) > 1:
    oitava = int(nota[1])
else:
    oitava = 4

# Gera a frequência
frequencia = 0

if nota_musical == "C":
    frequencia = 261.63
elif nota_musical == "D":
    frequencia = 293.66
elif nota_musical == "E":
    frequencia = 329.63
elif nota_musical == "F":
    frequencia = 349.23
elif nota_musical == "G":
    frequencia = 392.00
elif nota_musical == "A":
    frequencia = 440.00
elif nota_musical == "B":
    frequencia = 493.88

# Relação entre oitavas
if oitava < 4:
    for x in range(4-oitava):
        frequencia *= 2
elif oitava > 4:
    for x in range(oitava-4):
        frequencia /= 2

# Imprime a resposta
print(f"Frequencia da nota musical {nota}: {frequencia} Hz.")
