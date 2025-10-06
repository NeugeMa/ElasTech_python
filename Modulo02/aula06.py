# Estrutura de Laços Condicionais
''' Dentro desse módulo temos duas formas de "condição": 
    1. Condicionais (if/else)
    2. Laços de Repetição (for/while) (While = enquanto) / (for = para)
'''
# Para uma variável dentro de uma determinada faixa, execute
for var in range(10):
    print(var) # Irá repetir o valor de 0 à 9 

for var in range(1, 10):
    print(var)

# Objetivo: Solicite 3x a nota de um aluno e faça a média dessas três notas
soma = 0 

for i in range(1, 4):
    nota = int(input(f"Informe sua nota {i}: ")) # Informe sua nota 1 (ex)
    soma = soma + nota

print(soma / 3)
