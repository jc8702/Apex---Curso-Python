# ex-03.py

if __name__ == '__main__':

    lista_de_strings = []
    lista_de_numeros = []
    valor = None

    while valor != 'pronto':
        valor = input("Digite um valor: ")
        if valor.isnumeric():
            lista_de_numeros.append(valor)
        else:
            lista_de_strings.append(valor)

    lista_de_strings.pop()

    print("= Lista de strings =")
    for string in lista_de_strings:
        print(f'* {string}')

    print('-'*20)

    print("= Lista de numeros =")
    for numero in lista_de_numeros:
        print(f'* {numero}')
