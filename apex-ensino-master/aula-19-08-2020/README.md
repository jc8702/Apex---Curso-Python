# Funções

Uma função é um bloco de código que é executado apenas quando é chamado e que pode ser usado em diversos trechos do código. O uso de funções facilita o reuso de código dentro de nossa aplicação, assim como uma maior modularidade.

```
def soma(primeiro_numero, segundo_numero):
    return primeiro_numero + segundo_numero

if __name__ == '__main__':
    num1 = int(input("Digite o primeiro número: ))
    num2 = int(input("Digite o segundo número: ))

    print(soma(num1, num2))
```

## Exercícios

1. Escreva uma função que receba uma lista com 3 números, e retorne o maior entre eles.

2. Escreva uma função que receba uma lista de 5 números, e retorne outra lista com os quadrados de cada número:
    * Lista de entrada: [4, 7, 3, 5, 2]
    * Lista de saída: [16, 49, 9, 25, 4]

3. Escreva uma função que receba uma lista de números, e retorne apenas os números ímpares

4. Escreva uma função que chame outra função

5. Escreva uma função que receba uma quantidade variável de argumentos, e imprima a quantidade de argumentos e quais foram esses argumentos

6. Escreva uma função que receba uma quantidade variável de argumentos por posição e imprima a quantidade de argumentos e quais foram esses argumentos e seus valores

7. Escreva uma função que receba 3 argumentos obrigatórios: `nome`, `valor` e `setor`. A função irá processar e retornar o salário de acordo com os argumentos passados. Haverá outros 2 argumentos opcionais: `horas_trabalhadas` e `porcentagem_de_comissao` que serão incluídas no cálculo, de acordo com o setor que for informado no argumento setor. As regras são as seguintes:
    * Funcionário do setor 1 tem seu salário igual ao argumento `valor`
    * Funcionário do setor 2 tem seu salário igual ao cálculo dos argumentos `valor * horas_trabalhadas`
    * Funcionário do setor 3 tem seu salário igual ao cálculo `(valor * (porcentagem_de_comissao / 100))`

    Exemplo de funcionário do setor 1:

    ```
    $ python ex-07.py
    Informe o nome do funcionário: João
    Informe o valor: 3000
    Informe o setor: 1

    Calculo do salário de João:
    Valor: 3000.00
    ```

    Exemplo de funcionário do setor 2:

    ```
    $ python ex-07.py
    Informe o nome do funcionário: Maria
    Informe o valor: 35
    Informe o setor: 2
    Informe a quantidade de horas trabalhadas: 40

    Calculo do salário de Maria:
    Valor: 1400
    Quantidade de horas trabalhadas: 40
    Valor da hora: 35
    ```

    Exemplo de funcionário do setor 3:

    ```
    $ python ex-07.py
    Informe o nome do funcionário: Paulo
    Informe o valor: 12589.23
    Informe o setor: 3
    Informe a porcentagem de comissão: 20

    Calculo do salário de Paulo:
    Valor: 12589.23
    Porcentagem de comissão: 20%
    Valor da comissão: 2517.85
    ```
