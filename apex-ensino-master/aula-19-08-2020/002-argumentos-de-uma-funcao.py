# parâmetro ou argumento
# tipos de passagem de parâmetro

def retorna_lista(palavra1, palavra2, palavra3):
    # lista = []
    # lista.append(palavra1)
    # lista.append(palavra2)
    # lista.append(palavra3)]

    return [palavra1, palavra2, palavra3]

def alterar(lista):
    lista.append(99)

if __name__ == '__main__':
    print(retorna_lista('Python', 'Java', 'Haskell'))
    lista_de_numeros = [1, 2, 3]

    alterar(lista_de_numeros)
    print(lista_de_numeros)
