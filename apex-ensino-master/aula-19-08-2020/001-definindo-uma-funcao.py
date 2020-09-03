
def soma(num1, num2, nome):
    print(nome)
    return num1 + num2

def mensagem():
    return "Olá"

def subtracao(num1, num2):
    return num1 - num2

if __name__ == '__main__':
    print(soma(10, 10, 'Python'))
    print(mensagem())
    print(subtracao(10, 5))


# Crie uma função que receba 3 palavras, e retorne uma lista dessas palavras
# Valor de retorno da função: ['Python', 'Java', 'Kotlin']