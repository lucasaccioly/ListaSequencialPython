# Criando uma lista de números inteiros
numeros = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9]

# Inicializando uma lista para armazenar os números únicos
unicos = []

# Percorrendo a lista de números
for numero in numeros:
    # Verificando se o número não está presente na lista de únicos
    if numero not in unicos:
        # Adicionando o número à lista de únicos
        unicos.append(numero)

# Exibindo a lista de números únicos
print("Lista original:", numeros)
print("Lista de números únicos:", unicos)