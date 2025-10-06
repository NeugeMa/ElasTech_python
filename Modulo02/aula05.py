# Estrutura de Laços Condicionais
''' Dentro desse módulo temos duas formas de "condição": 
    1. Condicionais (if/else)
    2. Laços de Repetição (for/while) (While = enquanto)
'''

# Objetivo: Sortear um número
'''
Sortei um número e salve ele dentro de uma variável, peça para o user escrever outro número que precise dar 
match com o número salvo. Enquanto o número for diferente o código não irá parar.
'''

numSorteado = 10 
numEscolido = int(input("Informe um número de 0 à 10: "))
while numEscolido != numSorteado:
    print("Você errou.. Tente novamente!")

    numEscolido = int(input("Informe um número de 0 à 10: "))
print("Você acertou, parabéns!")

# Ex: Estrutura com contador
contador = 0
while contador < 5:
    print(contador)

    contador = contador + 1 # A cada laço, ele incrementará + 1
    


