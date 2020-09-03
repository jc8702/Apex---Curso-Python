# ex-07.py

def retorna_dicionario():
    return {'backend': 'Python', 'frontend': 'VueJS', 'database': 'PostgreSQL', 'cache': 'Redis'}

if __name__ == '__main__':

    valor = input("Digite o valor: ")

    print(retorna_dicionario())

    if valor in retorna_dicionario().values():
        print(f'{valor} é um valor do dicionário')

