frase = input("Digite uma frase: ")

# Quebra a frase em palavras
palavras = frase.lower().split()

# Dicionário para armazenar a frequência
frequencia = {}

# Conta a frequência de cada palavra
for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

# Exibe o resultado
for palavra, contagem in frequencia.items():
    print(f"'{palavra}': {contagem}")