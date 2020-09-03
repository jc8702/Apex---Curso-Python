# Exercício 02
# Escreva um programa em Python em que o usuário precise informar uma idade, em seguida retorne se a idade informada
# pertence a uma pessoa maior de idade. Pessoas maiores de idade serão consideradas caso a idade seja 18 ou superior.

if __name__ == '__main__':
    idade = int(input("Digite a sua idade: "))

    if idade >= 18:
        print("A pessoa é maior de idade.")
    else:
        print("A pessoa não é maior de idade.")