# ex-05.py

if __name__ == '__main__':
    
    palavra = ''
    lista_de_palavras = []

    while palavra != 'pronto':
        palavra = input('Digite uma palavra: ')
        lista_de_palavras.append(palavra)

    lista_de_palavras.pop()
    dicio = dict.fromkeys(lista_de_palavras, None)

    print(dicio)
