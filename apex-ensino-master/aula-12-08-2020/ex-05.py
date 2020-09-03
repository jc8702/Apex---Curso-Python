# Exercício 05
# Escreva um programa Python que peça o nome de um produto e o valor. Se o valor do produto for de R$ 100,00 ou superior,
# exiba uma frase com o nome do produto e um desconto de 10%. caso contrario exiba o nome do produto we seu valor integral.

if __name__ == '__main__':
    nome_do_produto = input("Digite o nome do produto: ")
    valor_do_produto = float(input("Digite o valor do produto: "))

    if valor_do_produto >= 100:
        valor_do_produto = valor_do_produto - (valor_do_produto * 0.1)

    print(f"O produto {nome_do_produto} vai custar {valor_do_produto}")