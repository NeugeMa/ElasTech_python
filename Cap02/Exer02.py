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


