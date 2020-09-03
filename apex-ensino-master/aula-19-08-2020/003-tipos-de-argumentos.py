# Argumentos obrigatórios
# Passagem de argumentos por posição e por nome
# Argumentos com valor padrão

def info_funcionario(setor, nome, salario, tempo_de_empresa = 1):
    return f'Nome: {nome} | Setor: {setor} | salario: {salario} | Tempo: {tempo_de_empresa}'

if __name__ == '__main__':
    print(info_funcionario('Maria', 'TI', 3000))
    print(info_funcionario('João', 'TI', 3000, 5))
    print(info_funcionario(tempo_de_empresa=2, nome='Paulo', setor='Vendas', salario=4000))
