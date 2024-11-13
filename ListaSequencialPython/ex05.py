# Criando uma lista de palavras
palavras = ["Casca de Bala", "La ele", "Bora bill", "Receba", "Tai Gostei", "Silem Mulambe Kaidros", "Allah"]

# Inicializando uma variável para contar as palavras que começam com 'A'
contagem = 0

# Percorrendo a lista de palavras
for palavra in palavras:
    # Verificando se a palavra começa com 'A'
    if palavra.lower().startswith('a'):
        # Incrementando a contagem
        contagem += 1

# Exibindo a contagem de palavras que começam com 'A'
print("Lista de palavras:", palavras)
print("Quantidade de palavras que começam com 'A':", contagem)