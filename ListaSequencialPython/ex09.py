# Criando duas listas de números inteiros
lista1 = [1, 2, 3, 4, 5, 6]
lista2 = [4, 5, 6, 7, 8, 9]

# Inicializando uma lista para armazenar os números comuns
comuns = []

# Percorrendo a primeira lista
for numero in lista1:
    # Verificando se o número está presente na segunda lista
    if numero in lista2:
        # Adicionando o número à lista de comuns
        comuns.append(numero)

# Exibindo os números comuns
print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Números comuns:", comuns)