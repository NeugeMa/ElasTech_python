# Nível 01 - Práticando


# Exercício 01
'''
Você trabalha em uma lojinha e precisa calcular o valor total da compra. 
O cliente comprou 3 produtos, e você deve:

- Pedir o preço de cada produto.
- Somar o total.
- Mostrar o valor final da compra.
'''
# Calculadora de compras
item01 = int(input("Digite o preço do item 01: "))
item02 = int(input("Digite o preço do item 02: "))
item03 = int(input("Digite o preço do item 03: "))

total =  item01 + item02 + item03
print("Sua compra deu o valor de R$",total)


# Exercício 02
'''
Você está criando um sistema para verificar o clima do dia. Peça a temperatura em graus Celsius.

- Se for menor que 18, diga “Está frio hoje!”.
- Se estiver entre 18 e 30, diga “Clima agradável!”.
- Se for maior que 30, diga “Está muito quente!”.
'''
# Verificador de temperatura
temperatura = int(input("Digite a temperatura de hoje: "))
if temperatura < 18: 
    print("Está frio hoje!")

elif temperatura > 18 or 30:
    print("Clima agradável!")

else:
    print("Está muito quente!")