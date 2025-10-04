# Exercício 01
'''
A instrução print(var3) exibe na tela o valor armazenado na variável var3, em cada uma das 
duas vezes que a instrução aparece no script acima. 

Para que os valores exibidos na tela sejam, nessa ordem, 42 e 21.0, quais operadores 
matemáticos devem substituir 'XXX' e 'YYY' no trecho de código, respectivamente?

var1 = 12
var2 = 30

var3 = var1 XXX var2
print(var3)

var3 = var3 YYY 2
print(var3)
'''

var1 = 12
var2 = 30 

var3 = var1 + var2
print(var3)
var3 = var3 / 2
print(var3)


# Exercício 02
'''
Algumas situações requerem que os dados sejam recebidos diretamente pelo usuário como parte 
da execução do programa. 

Isso pode ser feito com a função input(). No entanto, esta função sempre retorna os valores 
em string. Assim, se os dados esperados do usuário forem numéricos, é importante realizar a 
conversão dos tipos de dados para que eles possam ser processados. 

Considere o trecho abaixo:

num1 = XXX
dobro = 2*num1

print("O dobro do número digitado é:", dobro)

Levando em consideração que o usuário pode entregar qualquer número como input, o 'XXX' no código acima 
deve ser substituído por qual elemento?
'''

num1 = int(input("Digite um número: "))
# OU num1 = float(input("Digite um número: "))
dobro = 2*num1
print("O dobro do número digitado é:", dobro)


# Exercício 03
'''
Para a construção de programas flexíveis e mais complexos, é necessário que haja a realização de comparações. 
Isso é possível com o uso de operadores lógicos de comparação (em python: ==, !=, <, <=, >, >=), como mostra o código:

x = 10
y = 4.2

num = float(input("Digite um número a seguir: "))
print(num > x*y, num <= x + y, num*y != x*y)

Suponha que na execução do script acima, o usuário digitou o valor 10, quando solicitado pelo input. 
Qual das alternativas a seguir produz o mesmo output que o script acima? 
'''

x = 10
y = 4.2

num = float(input("Digite um número a seguir: "))
print(num > x*y, num <= x + y, num*y != x*y)