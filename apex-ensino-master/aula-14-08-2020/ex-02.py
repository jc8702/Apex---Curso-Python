
if __name__ == '__main__':
    lista_de_numeros = [5, 90, 51, 23, 54, 1, 8, 16, 24, 55]
    indice = 0

    for numero in lista_de_numeros:
        if numero > 50:
            print(f'{indice}: {numero}')
        indice = indice + 1