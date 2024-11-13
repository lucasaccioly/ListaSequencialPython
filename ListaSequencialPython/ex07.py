# Criando uma lista de números inteiros
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Inicializando uma lista para armazenar os números pares
pares = []

# Percorrendo a lista de números
for numero in numeros:
    # Verificando se o número é par
    if numero % 2 == 0:
        # Adicionando o número à lista de pares
        pares.append(numero)

# Exibindo os números pares
print("Lista de números:", numeros)
print("Números pares:", pares)