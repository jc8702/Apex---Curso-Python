
# Algoritmo que calcula a comissão de uma venda
# Se o valor da comissão for maior que R$ 1000, é acrescido um bônus de 100 R$ ao valor final

def calcular_comissao(valor_da_venda, porcentagem_comissao):
    valor_comissao = (valor_da_venda * porcentagem_comissao) / 100
    return valor_comissao

def calcular_valor_final(valor_comissao):
    if valor_comissao > 1000:
        print("Adicionado 100 ao valor final")
        return valor_comissao + 100


if __name__ == '__main__':

    # valores de entrada
    valor_da_venda = 10000
    porcentagem_comissao = 30
    valor_final = 0

    # processamento
    valor_comissao = calcular_comissao(valor_da_venda, porcentagem_comissao)
    valor_final = calcular_valor_final(valor_comissao)

    # saida
    print(f"{valor_final:.2f}")