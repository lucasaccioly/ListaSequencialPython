# Criando uma lista de números inteiros
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Inicializando uma lista para armazenar os números ímpares
impares = []

# Percorrendo a lista de números
for numero in numeros:
    # Verificando se o número é ímpar
    if numero % 2 != 0:
        # Adicionando o número à lista de ímpares
        impares.append(numero)

# Exibindo os números ímpares
print("Lista de números:", numeros)
print("Números ímpares:", impares)