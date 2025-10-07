# Estruturas de Listas
# Uma variável que consegue armazenar outros tipos dentro dela

i = [] # Ex de lista vazia
i = list() # Ex de outro tipo, de lista vazia

# Objetivo: Armazenar 3 notas à uma lista 
notas = [7.9, 10, 5.6] 
print(notas)

# Indexação
lista = [20, 'Mariana', 1.60, True]
print(lista[0]) # Acessando informações específicas de uma lista
print(lista[1])
print(lista[2])
print(lista[3])

# Slices
lista = [1, 2, 3, 4, 5]
print(lista[0:3]) # Apenas pegará as info (1,2,3)

# Iterações com FOR

# Utilizando elementos da lista
for elemento in lista:
    print(elemento)

# Utilizando indices
print('Comprimento da lista', len(lista)) # len = quantidade de elementos
for i in range(len(lista)):
    print(i)