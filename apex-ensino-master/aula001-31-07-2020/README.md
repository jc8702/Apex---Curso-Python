# Python - Conceitos

### Executando um script Python
Por boa prática, nos arquivos python sempre definimos uma seção onde o código será executado se o arquivo estiver sendo chamado diretamente, pelo terminal ou por alguma IDE:

```python

if __name__ == '__main__':
    print("Hello world.")
```

### Operadores
* Aritméticos: + - * / % ** //
* Atribuição: = += -= *= /=
* Comparação: == != > < >= <=
* Lógicos: and or not
* Identidate: is is not
* Pertencimento: in not in

### Entrada e saída
Para receber e imprimir informações pelo terminal, usamos os `built-ins` `input()` e `print()`, respectivamente:

```python
if __name__ == '__main__
    nome = input("Digite o seu nome: ")
    print(nome)
```
`input()` recebe um argumento, que é o texto que será mostrado no terminal.
`print()` recebe o texto ou a variável que será impressa.


### Tipos de dados
Tipos texto:
* `str` - Tipo que representa uma string
    ```python
    if __name__ == '__main__':
        nome_curso = "Python"
        print(nome_curso)
    ```

    Se quisermos representar uma string multi linha, devemos usar `"""`:
    ```python
    if __name__ == '__main__':
        mensagem = """
        Seja bem vindo!
        Python 2020.
        """
        print(mensagem)
    ```

    Uma string em Python pode ser entendida como uma lista de caracteres, e dessa maneira podemos acessar uma posição em específico dessa lista:
    ```python
    if __name__ == '__main__':
        mensagem = "Apex Ensino"
        print(mensagem[3])
    ```

    Quando queremos formatar de uma maneira diferente nossa string, seja com uma nova linha ou com um TAB, usamos as constantes de caractere especial:
    ```python
    if __name__ == '__main__':
        mensagem = "Python\nVueJS\nJavascript"
        print(mensagem)
    ```

    Também podemos usar uma sintaxe especial quando quisermos imprimir o valor de uma variável junto com um texto. Chamamos essa sintaxe especial de `f-strings`:
    ```python
    if __name__ == '__main__':
        numero1 = 1
        numero2 = 4
        resultado = numero1 + numero2

        print(f"O resultado da soma é {resultado}")
    ```

    Ou podemos usar também o método de string `format`:
    ```python
    if __name__ == '__main__':
        numero = 3
        print("{} x {} = {}".format(3, 3, 3 * 3))
    ```

    Também podemos ignorar qualquer caractere ou marcação especial usando as `raw strings`:
    ```python
    if __name__ == '__main__':
        texto = r"Os\n caracter\tes especiais\n\n serão \rignorados"
        print(texto)
    ```

    Como tudo em Python é considerado um objeto, temos diversas funções para manipulação e transformação de strings. Por exemplo:
    ```python
    if __name__ == '__main__':
        # Transformar todas as letras em maiúsculas
        print("esse texto deve estar todo em maíusculo".upper())

        # Preencher a string com zeros à esquerda até a string ter o tamanho 5
        print("456".zfill(5))
    ```

    Para uma referência completa sobre todas as funções de strings do Python, consulta a documentação oficial: https://docs.python.org/3/library/stdtypes.html#string-methods.

    

Tipos númericos
* `int`, `float`, `complex`
O tipo `int` representa o tipo número inteiro, sem casas decimais. Podem ser positivos ou negativos.
```python
if __name__ == '__main__':
    numero1 = 5654.14985945238102843795847529306857293085743289

    print(f"O quadrado de {numero} é {(numero * numero):.2f}")
```
O tipo `float` representa o tipo número de ponto flutuante, com casas decimais. Pode ser positivo ou negativo.


### Controle de decisão com if-elif-else


### Controle de repetição com for/while

### funções
