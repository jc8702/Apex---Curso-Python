from graus import ABAIXO_DO_PESO, ACIMA_DO_PESO


def calcular(altura, peso):
    imc = peso / (altura * altura)

    if imc <= ABAIXO_DO_PESO:
        print("Você está abaixo do peso.")
    elif imc >= ACIMA_DO_PESO:
        print("Você está acima do peso.")
    else:
        print("Você está no seu peso ideal.")