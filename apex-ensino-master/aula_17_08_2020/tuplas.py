
# Tuplas (list)
# É uma coleção de dados que é ordenável e imutável. Permite duplicação

if __name__ == '__main__':
    lista_de_compras = ('Abacaxi', 'Uvas', 'Manga', 'Morango', 'Coco',)

    for item in lista_de_compras:
        print(item)

    print('-'*10)

    # Podemos acessar os itens de uma tupla pelo seu índice
    # Em python, o índice sempre começa em 0
    print(lista_de_compras[1])

    # Também podemos usar índices negativos. O índice -1 se refere ao último item, o -2 ao penúltimo, e assim por diante
    print(lista_de_compras[-1])

    # Também podemos "fatiar" uma tupla, retornando uma parte dela, usando os índices. Chamamos isso de slice
    print(lista_de_compras[2:4])
    print(lista_de_compras[2:])
    print(lista_de_compras[:])
    
    # NÃO podemos alterar um item em específico de uma tupla acessando o seu índice
    # Tuplas são objetos imutáveis
    lista_de_compras[1] = 'Abacate'
    print(lista_de_compras)

    # Podemos checar se um determinado item existe em uma tupla, usando o operador in
    print('Manga' in lista_de_compras)

    # Podemos usar algumas funções built-ins do Python em tuplas. Um exemplo é a função len(), que usamos pra verificar o tamanho de uma lista
    print(len(lista_de_compras))

    # Funções de tuplas

    # count()	Retorna a quantidade de vezes que um valor se repete em uma lista
    # index()	Retorna a posição da primeira ocorrência do item que foi expecificado
