# ex-02.py

if __name__ == '__main__':

    valor = None
    lista_de_valores = []
    indice = 1

    while valor != 'sair':
        valor = input("Digite um valor: ")
        lista_de_valores.append(valor)

    lista_de_valores.pop()

    for valor in lista_de_valores:
        print(f"{indice}. '{valor}'")
        indice += 1
