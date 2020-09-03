# ex-07.py
from aula_17_08_2020.ex08 import retorna_dicionario

if __name__ == '__main__':

    chave = input("Digite o chave: ")

    if chave in retorna_dicionario().keys():
        print(f'{chave} é um chave do dicionário')

