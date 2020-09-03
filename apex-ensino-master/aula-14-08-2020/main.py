
if __name__ == '__main__':

    # for
    # O laço for é usado quando queremos percorrer uma sequência de itens: Uma string ou uma lista, por exemplo.
    # Basicamente, usamos o for em qualquer objeto que seja *iterável*
    # A cada passo, o for tem acesso a um item da sequência
    lista_de_compras = ['Uvas', 'Manga', 'Abacaxi']

    for item in lista_de_compras:
        print(f'Item da lista: {item}')

    lista_de_numeros = [2, 76, 23, 1, 8, 25]
    for numero in lista_de_numeros:
        print(numero ** 2)

    # Quando queremos, por qualquer motivo, parar a execução do laço for, usamos a declaração break
    # Se o item da lista de compras for diferente de uma string, paramos a execução
    lista_de_compras.insert(2, 10)

    for item in lista_de_compras:
        if not isinstance(item, str):
            print("Encontrado um tipo estranho")
            break

    texto = "Apex Ensino curso de Python"

    for letra in texto:
        if letra == 'n':
            print("Encontrada a letra n")


    # Quando queremos, por qualquer motivo, parar a execução da iteração atual e continuar para a próxima
    # utilizamos a declaração continue
    for item in lista_de_compras:
        # se o item atual não for do tipo str
        if not isinstance(item, str):
            continue
            print("Nao deve mostrar")
    
    # Também podemos "encadear" um laço for dentro de outro, indefinidamente
    for x in range(10):
        for y in range(10):
            print(f'{x} - {y}')

    # Junto com o for, podemos usar o else, pra sempre executar alguma ação quando o loop for for encerrado.
    for item in []:
        print(f"Item da lista: {item}")

    else:
        print("Lista verificada.")

    # while
    # O laço while é usado sempre que desejarmos executar um conjunto de instruções e enquanto uma determinada condição for verdadeira

    from random import randint

    valor = 0
    while valor < 10:
        valor_randomico = randint(1, 3)
        valor = valor + valor_randomico
    else:
        print("O valor foi atingido")



    # break

    # continue

    # else