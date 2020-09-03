
# Dicionários (dict)
# É uma coleção de dados que é mutável e indexável. Permite duplicação apenas de valores

if __name__ == '__main__':
    armazem = {
        'Parafuso': 44995,
        'Óleo': 234,
        'Motor': 27, 'Placa': 2856, 'Circuito': 1174
    }

    for item in armazem:
        print(item)

    print('-'*10)


    # Podemos checar se uma determinada chave existe em um dicionário, usando o operador in
    print('Manga' in armazem.keys())

    # Podemos usar algumas funções built-ins do Python em dicionparios. Um exemplo é a função len(), que usamos pra verificar o tamanho de um dicionário
    print(len(armazem))

    # Funções de dicionários

    # clear()	    Remove todos os elementos de um dicionário
    #armazem.clear()
    #print(armazem)

    # copy()	    Retorna uma cópia do dicionário
    #armazem2 = armazem
    #armazem['Parafuso'] = 1000

    # fromkeys()	Retorna um dicionário com as chaves e o valor que for especificado
    estados = dict.fromkeys(('sc', 'sp', 'mg', 'rj'), 0)
    print(estados)

    # get()	        Retorna o valor da chave informada
    print(estados.get('r', 'rn'))
    #print(estados['r'])

    # items()	    Retorna uma lista de tuplas de chave/valor
    print(armazem.items())
    print("ITENS NO ARMAZÉM")
    for chave, valor in armazem.items():
        print(f"Item: {chave} | Quantidade: {valor}")

    # keys()	    Retorna uma lista contendo as chaves de um dicionário
    for key in armazem.keys():
        print(key)

    # pop()	        Retorna e remove o elemento com a chave especificada
    print(armazem.pop('Parafuso'))
    print(armazem)

    # popitem()	    Remove o último par chave/valor de um dicionário
    armazem.popitem()
    print(armazem)

    # setdefault()	Retorna o valor da chave especificada. Se a chave não existir, insere a chave e o valor especificado.
    print(estados.setdefault('sc', 'novo'))
    print(estados)

    # update()	    Atualiza o dicionário com os valores cha/valor especificados
    estados.update({'sc': 'sul'})
    estados.update({'am': 'norte'})
    print(estados)

    # values()	    Retorna uma lista com os valores de um dicionário
    for value in armazem.values():
        print(value)
