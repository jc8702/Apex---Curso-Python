# ex-01.py
# dica: Use a função sum
from random import randint

if __name__ == '__main__':

    lista_de_numeros = [12, 4, 32, 19, 10, 3, 20, 1, 9, 11]
    valor_total = 0

    for numero in lista_de_numeros:
        valor_total += numero

    print(valor_total)

    # Usando sum()
    print(sum(lista_de_numeros))
