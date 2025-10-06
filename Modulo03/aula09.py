# Funções
# Um bloco de código que pode ser reutilizado várias vezes

# Iniciando com uma função simples
def saudacao():
    print("Olá, seja bem-vindo!")

saudacao()  # Chamada da função

# Parâmetros
def saudacao(nome, curso): # nome/curso é um parâmetro
    print(f"Olá, {nome}, seja bem-vindo!")
    print(f"Você está matriculado no {curso}.")

saudacao("Mari", "Curso de Python") # chamada da função com argumento

