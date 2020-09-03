# Exercício 01
# Peça um nome e uma idade, em seguida exiba uma frase, como por exemplo: Olá, João. Você tem 16 anos.

if __name__ == '__main__':
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite a sua idade: "))

    print(f'Olá {nome}, você tem {idade} anos')