# Exercício 01
'''
É muito frequente o uso de programação para a automação de tarefas repetitivas, sendo possível devido às 
estruturas de repetição. 

Em python, uma dessas estruturas é o laço while, que determina que um bloco de código seja repetido enquanto 
uma dada condição for verdadeira. Observe o código a seguir:

cont = 0
resultado = 0
n = 1000

while cont != n:

    resultado = resultado + 1/(2**cont)

    cont = cont + 1

print(resultado)

Ao ser executado, o que o trecho de código acima mostra na tela?
'''

cont = 0
resultado = 0
n = 1000

while cont != n:
    resultado = resultado + 1/(2**cont)
    cont = cont + 1
print(resultado)


# Exercício 02
'''
Além do laço de repetição while, muitas vezes utilizamos o operador for em Python para implementarmos 
laços de repetição. 

Embora isso seja possível, o for é mais do que meramente um laço de repetição: este operador é utilizado para 
percorrer alguma estrutura iterável. 

for _ in range(10):
   print("Olá, mundo!")

Quando queremos utilizar o for explicitamente como um laço de repetição, é muito comum utilizarmos a 
estrutura acima, com o auxílio do iterador range(). 
No entanto, o mesmo comportamento é possível se nos aproveitarmos do fato de que o for percorre qualquer iterável. 
Sabendo disso, das alternativas a seguir, qual é a única que NÃO reproduz o mesmo resultado que o trecho acima?
'''


# Exercício 03
'''
Utilizamos listas para armazenar em um único objeto uma coleção de valores. Muitas vezes, desejamos criar 
uma nova lista a partir de uma lista original. Observe o código abaixo:

lista_inicial = [10, 5, -7, 6, -42, 63, -8, -5, 13]
lista_final = []

for item in lista_inicial:

    if item % 2 == 0:
        if item < 0:
            lista_final.append(A)
    
        else:
            lista_final.append(B)
    else:
        if item < 0:
            lista_final.append(C)
    
        else:
            lista_final.append(D)

Qual deve ser o valor de A, B, C e D, respectivamente, para que o código acima gere a seguinte lista_final: 
[10, 10, 14, 6, 42, 126, 8, 10, 26]?
'''