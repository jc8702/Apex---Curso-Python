# Exercício 06
# Escreva um programa Python que pedirá 3 números, informe qual deles é o menor.

if __name__ == '__main__':
    numero1 = int(input("Digite o primeiro número: "))
    numero2 = int(input("Digite o segundo número: "))
    numero3 = int(input("Digite o terceiro número: "))

    numeros = [numero1, numero2, numero3]
    numeros.sort()

    if numero1 < numero2 and numero1 < numero3:
        print(f"O menor número é o primeiro: {numero1}")

    elif numero2 < numero1 and numero2 < numero3:
        print(f"O menor número é o segundo: {numero2}")

    elif numero3 < numero1 and numero3 < numero2:
        print(f"O menor número é o segundo: {numero3}")
