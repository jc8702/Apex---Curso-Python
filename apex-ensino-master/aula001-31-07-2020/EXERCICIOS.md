# Exercícios

1. Escreva uma função que receba a altura e o peso de uma pessoa, e com essas informações faça o cálculo do IMC. A fórmula para cálculo do IMC de uma pessoa é a seguinte: IMC = peso/(altura * altura)
2. Escreva uma função que receba um número randômico de 1 a 100. Imprima no terminal se o número é par ou impar.
3. Escreva uma função que receba uma lista de números, e retorne outra lista com o quadrado desses números.
4. Escreva uma função que receba uma lista com 5 notas de um competidor Essa função irá calcular a média de pontos desse competidor, porém irá excluir a maior e menor notas.
5. Escreva uma função que receba uma lista de itens representando cursos. Se nessa lista houver a palavra "Python", imprima "Encontrado Python". Senão, imprima "Python não encontrado".
6. Escreva uma função que receba uma lista de dicionários, com cada dicionário sendo a representação de um item de compra, com nome, quantidade e valor. Imprima essa lista de itens no terminal no seguinte formato:
* `Item: <nome_do_item> | Quantidade: <quantidade_do_item> | Valor unitário: <valor_unitario_do_item>`
* `Item: <nome_do_item> | Quantidade: <quantidade_do_item> | Valor unitário: <valor_unitario_do_item>`
7. Escreva um programa que simule uma batalha entre um guerreiro e um monstro. A função de entrada vai receber 2 dicionários: Um que representa o guerreiro, e o outro que representa o monstro. Os dicionários vão ter as seguintes chaves, que vão representar cada uma das entidades: Nome, HP, Ataque e Defesa. Enquanto o HP de nenhum dos personagens chegar a 0, a batalha continuará. Em cada fase da batalha, o algoritmo vai testar a força de ataque e a força de defesa de cada personagem, adicionando um valor randômico a esse teste. A diferença vai definir quanto de dano um personagem tirou do outro. Por exemplo:

    ```
    Guerreiro possui 6 de ataque
    Monstro possui 5 de defesa
    Guerreiro ataca monstro com ataque(6) + 3
    Monstro defende com defesa(5) + 1
    Monstro sofreu 3 de dano
    ```

8. Escreva um programa que simule uma vending machine. Cada prateleira da vending machine será representada por uma lista de espaços, e cada espaço terá um número e uma lista de itens. O programa deve pedir para o usuário digitar o número do item que ele quer pegar, com isso o programa vai verificar se há itens no espaço correspondente ao número que o usuário digitou. Se houver itens, o item é retirado da lista e retornado ao usuário. Se não houver itens, o programa vai mostrar uma mensagem de que não há mais itens e vai pedir um novo número ao usuário.