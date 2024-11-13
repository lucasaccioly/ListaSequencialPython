# Criando uma lista de strings
palavras = ["Spark a blunt", "SeshHollowWaterBoys", "ArizonaIcedOutBoysClub", "Lucki me, i see demons", "I swear i love these bitches im' a feminist.", "Gothboiclique", "Keep a small circle, ion' fuck with squares."]

# Inicializando uma variável para armazenar a palavra mais longa
mais_longa = ""

# Percorrendo a lista de palavras
for palavra in palavras:
    # Verificando se a palavra é mais longa que a atual mais longa
    if len(palavra) > len(mais_longa):
        # Atualizando a palavra mais longa
        mais_longa = palavra

# Exibindo a palavra mais longa
print("Lista de palavras:", palavras)
print("Palavra mais longa:", mais_longa)