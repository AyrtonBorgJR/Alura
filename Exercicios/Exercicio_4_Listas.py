### 1 - Crie uma lista para cada informação a seguir:

#Lista de números de 1 a 10;
#Lista com quatro nomes;
#Lista com o ano que você nasceu e o ano atual.

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l2 = ["Sebastian", "Laura", "Nadia", "Ayrton"]
l3 = [1991, 2025]

#2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.
for i in l2:
    print(i)

#3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.
tot = 0
for i in l1:
    if i % 2 == 1:
        tot = i + tot
print(tot)

#4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

for i in reversed(l1):
    print(i)

#5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.
tabuada = int(input("Escolha um numero de 1 a 10: "))
for i in range(1, 11):
    print(f'{tabuada} x {i} = {tabuada * i}')

#6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. 
## - Utilize um bloco try-except para lidar com possíveis exceções.

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l1.append("pinto")

tot = 0
for item in l1:
    try:
        tot += int(item)  # Tenta converter para número
    except ValueError:
        print(f"O item {item} não é um número válido. Será desconsiderado da soma")

print(tot)
print(l1)
#7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

l90 = [1, 2, 3, 4, 5, 6, 10]

div = 0
test = 0
for num in l90:
    try:
        test += int(num)  # Tenta converter para número
        div = div +1
    except ValueError:
        print("kkk")

print (div)