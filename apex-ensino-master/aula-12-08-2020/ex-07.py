# Exercício 07
# Escreva um programa Python que peça 2 valores e um tipo de cálculo (soma, subtração, multiplicação ou divisão).
# Efetue o cálculo e exiba.

if __name__ == '__main__':
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    tipo_de_operacao = input("Digite o tipo da operação: ")

    if tipo_de_operacao == 'soma':
        print(f'Resultado: {valor1 + valor2}.')

    elif tipo_de_operacao == 'subtracao':
        print(f'Resultado: {valor1 - valor2}.')

    elif tipo_de_operacao == 'multiplicacao':
        print(f'Resultado: {valor1 * valor2}.')

    elif tipo_de_operacao == 'divisao':
        print(f'Resultado: {valor1 / valor2}.')

    else:
        print("Tipo de operação desconhecida.")
