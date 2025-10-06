# Métodos e Funções de Lista 
# Para utilizar um método você precisa atralear ele a uma variável

lista = [1, 3, 12, 8, 2]
print(lista)

# Append (sempre no final da lista)
lista.append(3)
print('Depois do append', lista)

# Insert (adiciona num local especifico)
lista.insert(2, 10) # (indice, valor)
print('Depois do insert', lista)

# Extend
lista2 = [4, 2, 3]
lista.extend(lista2)
print('Depois do extend', lista)

# Pop (remove o ultimo elemento)
lista.pop()
print('Depois do pop', lista)

# Remove
lista.remove(3) # Remove o primeiro elemento que encontrar

# Count (Conta quantos elementos iguais existem na lista)
print('Quantidade de 3 na lista', lista.count(3))

# Index 
print('Indice do elemento 8', lista.index(8)) # Retorna o indice do elemento

# Sort (Ordena a lista)
lista.sort()

# len
print(len(lista)) # Quantidade de elementos na lista

# sum
print(sum(lista)) # Soma todos os elementos da lista

# max
print(max(lista)) # Retorna o maior elemento da lista

# min 
print(min(lista)) # Retorna o menor elemento da lista

