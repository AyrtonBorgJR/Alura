#1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

num = int(input("Diigte um numero: "))
if num % 2 == 0:
    print("Esse é um numero par")
else:
    print("Esse é um numero impar")

# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

idade = int(input("Me diga quantos anos você tem: "))

if 0 < idade <= 12:
    print("Você é uma criança.")
elif 13 <= idade <= 18:
    print("Você é um adolescente.")
else:
    print("Você é um adulto.")