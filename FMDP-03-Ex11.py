# Importa a biblioteca math

import math

# Solicita os valores de a, b e c

a = float(input("Insira o valor de a: "))
b = float(input("Insira o valor de b: "))
c = float(input("Insira o valor de c: "))

# Limita o valor de a

while True:
    if a != 0:
        break
    print("Valor inválido, tente novamente.")
    a = float(input("Insira o valor de a: "))

# Gera o discriminante

delta = b**2 - 4*a*c

# Verifica se há raízes reais

if delta < 0:
    print("A função não possui raízes reais.")
elif delta == 0:
    x = -b / (2*a)
    print(f"A função possui uma raiz real: {x}.")
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"A função possui duas raízes reais: {x1} e {x2}.")