# Exercício 03
# Escreva um programa Python que peça duas notas, em seguida exiba a média.

if __name__ == '__main__':
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2) / 2

    print(f"Sua média é de {media}")
