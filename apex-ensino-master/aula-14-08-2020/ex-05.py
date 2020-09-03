

if __name__ == '__main__':
    numero = int(input("Digite um número: "))

    multiplicador = 1

    while multiplicador <= 10:
        print(f"{numero} x {multiplicador} = {numero * multiplicador}")
        multiplicador = multiplicador + 1
