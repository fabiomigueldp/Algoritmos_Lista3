'''3. Vogal ou consoante. Escreva um programa Python que peça para o usuário uma letra do
alfabeto. Se o usuário entrar com as letras a, e, i, o ou u, o programa deve exibir uma
mensagem dizendo que a letra é uma vogal. Caso contrário, o programa deve exibir a
mensagem informando que a letra é uma consoante.'''

# Solicita a letra

letra = input("Insira uma letra do alfabeto: ")

# Verifica se a letra é vogal ou consoante

if letra in ('a', 'e', 'i', 'o', 'u'):
    print("A letra é uma vogal.")
else:
    print("A letra é uma consoante.")