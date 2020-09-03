# ex-04.py

if __name__ == '__main__':

    banco_de_dados = []
    comando = None

    menu = """
    * adicionar: Adiciona um registro
    * excluir: Exclui um registro
    * diminuir: Exclui o último registro feito
    * mostrar: Mostra os dados
    * sair: Sai.
    """

    print(menu)

    while comando != 'sair':
        comando = input("O que você deseja fazer? ")

        if comando == 'adicionar':
            valor = input("Digite o que deseja adicionar: ")
            banco_de_dados.append(valor)
            print(f"'{valor}' adicionado com sucesso.")

        elif comando == 'excluir' and len(banco_de_dados) > 0:
            valor = input("Digite o que deseja excluir: ")
            banco_de_dados.remove(valor)
            print(f"'{valor}' removido com sucesso.")

        elif comando == 'diminuir':
            if len(banco_de_dados) > 0:
                print(f'Registro excluído: {banco_de_dados.pop()}')
            else:
                print("Não há dados a serem excluídos do banco.")

        elif comando == 'mostrar':
            print(banco_de_dados)

    print("Tchau!")
