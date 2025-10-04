# Estruturas Condicionais
''' Dentro desse módulo temos duas formas de "condição": 
    1. Condicionais (if/else)
    2. Laços de Repetição (for/while)
'''

# Objetivo: Verificar a idade da pessoa
idade = int(input("Digite sua idade: "))
if idade >= 18: # if (se)
    print("Você tem mais que 18 anos!")
else: 
    print("Você é de menor ainda :(")

# Outro jeito de fazer 
numIdade = 20 # Criando uma variável
if numIdade >= 18: 
    print("Você tem mais que 18 anos!")
else: 
    print("Você é de menor ainda :(")

# Desafio!
''' Imagine que você queira imprimir "Aprovado", caso o estudante tenha uma média superior/igual à 7, e
    "Reprovado", caso a média seja inferior a 7. 
'''
nota = int(input("Digite sua nota: "))
if nota >= 7: 
    print("Aprovado!")
else: 
    print("Reprovado!")

# Adicionando o Elif para uma segunda condição 
''' Imagine que você queira imprimir "Aprovado", caso o estudante tenha uma média superior/igual à 7, 
    "De Recuperação", caso o estudante tenha tirado 6 e "Reprovado", caso a média seja inferior a 7. 
'''
nota = int(input("Digite sua nota: "))
if nota >= 7: 
    print("Aprovado!")
elif nota == 6: # Operador de igual (==)
    print("Recuperação!")
else: 
    print("Reprovado!")
