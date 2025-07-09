#7 - Construa um código que calcule a média dos valores em uma lista. 
## - Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.
lista = [0]
soma = 0
contagem = 0

for valor in lista:
    try:
        soma += float(valor)
        contagem += 1
    except (ValueError, TypeError):
        print(f"Valor inválido ignorado: {valor}")

try:
    media = soma / contagem
    print(f"Média: {media:.2f}")
except ZeroDivisionError:
    print("Erro: Lista vazia ou sem valores válidos.")