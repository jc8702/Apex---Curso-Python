
# Listas (list)
# É uma coleção de dados que é ordenável e mutável. Permite duplicação
# Coleções são objetos iteráveis

if __name__ == '__main__':
    lista_de_compras = ['Abacaxi', 'Uvas', 'Manga', 'Morango', 'Coco']

    for item in lista_de_compras:
        print(item)

    print('-'*10)

    # Podemos acessar os itens de uma lista pelo seu índice
    # Em python, o índice sempre começa em 0
    print(lista_de_compras[1])

    # Também podemos usar índices negativos. O índice -1 se refere ao último item, o -2 ao penúltimo, e assim por diante
    print(lista_de_compras[-1])

    # Também podemos "fatiar" uma lista, retornando uma parte dela, usando os índices. Chamamos isso de slice
    print(lista_de_compras[2:4])
    print(lista_de_compras[2:])
    print(lista_de_compras[:])
    
    # Podemos alterar um item em específico de uma lista acessando o seu índice
    lista_de_compras[1] = 'Abacate'
    print(lista_de_compras)

    # Podemos checar se um determinado item existe em uma lista, usando o operador in
    print('Manga' in lista_de_compras)

    # Podemos usar algumas funções built-ins do Python em listas. Um exemplo é a função len(), que usamos pra verificar o tamanho de uma lista
    print(len(lista_de_compras))

    # Métodos de listas
    print("-"*20)

    # append()	Adiciona um elemento no fim de uma lista
    lista_de_compras.append('Jabuticaba')
    #print(lista_de_compras)

    # clear()	Remove todos os elementos de uma lista
    #lista_de_compras.clear()
    #print(lista_de_compras)

    # copy()	Retorna uma cópia de uma lista
    lista_de_mercado = lista_de_compras.copy()
    lista_de_mercado.append('Carne')
    print(lista_de_compras)
    print(lista_de_mercado)

    # count()	Retorna a quantidade de vezes que um valor se repete em uma lista
    lista_de_compras.append('Manga')
    print(lista_de_compras.count('Manga'))

    # extend()	Adiciona os elementos de uma lista(ou de um iterável) ao final da lista
    acougue = ['Linguiça', 'Pescoço', 'Frango']
    lista_de_compras.extend(acougue)
    print(lista_de_compras)

    # index()	Retorna a posição da primeira ocorrência do item que foi expecificado
    print(lista_de_compras.index('Manga'))

    # insert()	Adiciona um elemento na posição especificada na lista
    lista_de_compras.insert(2, 'Pitanga')
    print(lista_de_compras)

    # pop()     Remove e retorna um elemento em uma posição específica da lista. Se nada for informado, remove e retorna o último

    print(lista_de_compras.pop(0))
    print(lista_de_compras)

    # remove()	Remove da lista o valor que foi especificado
    lista_de_compras.remove('Manga')
    print(lista_de_compras)

    # reverse()	Inverte a ordem de uma lista
    numeros = [1, 2, 3, 4, 5]
    numeros.reverse()
    print(numeros)
    lista_de_compras.reverse()
    # sort()	Organiza uma lista
    lista_de_compras.sort()
    print(lista_de_compras)

[2, 65, 525, 76, 23423, 4354656]