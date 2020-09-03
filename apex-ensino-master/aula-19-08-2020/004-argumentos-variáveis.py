# Podem ser chamados também de argumentos arbitrários
# Desempacotando listas
# Desempacotando dicionários

def info_funcionario(setor, nome, salario, tempo_de_empresa = 1):
    return f'Nome: {nome} | Setor: {setor} | salario: {salario} | Tempo: {tempo_de_empresa}'

data = {
    "setor": "Human Resources",
    "nome": "Maria",
    "salario": 2300.0,
    "tempo_de_empresa": 10
}

if __name__ == '__main__':
    # **data = unpacking
    print(info_funcionario(*['TI', 'Mario', 3000]))
    #print(info_funcionario(data['setor'], data['nome']))