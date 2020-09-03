# Exercício 04
# Escreva um programa Python que peça três notas, informe a média e a situação do aluno. Caso a média seja 7 ou superior
# o aluno estará aprovado, caso contrário, reprovado.

if __name__ == '__main__':
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    media = (nota1 + nota2 + nota3) / 3

    if media < 5:
        print(f"Média final: {media:.2f}. O aluno está reprovado")

    # else if
    elif media >= 5 and media < 7:
        print(f"Média final: {media:.2f}. O aluno está de recuperação")

    else:
        print(f"Média final: {media:.2f}. O aluno está aprovado")
