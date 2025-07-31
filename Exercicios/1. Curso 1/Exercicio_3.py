#3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar,
#se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

from app import exibir_nome

usuario = "Ayrton"
senha = "21091991"

while True:
    login = input("Digite seu usuário(Seu Nome): ")  # Solicita o login
    if login == usuario:
        break  # Sai do loop se estiver correto
    else:
        print("Erro: Login inválido. Tente novamente.")

while True:
    senha_log = input("Insira sua senha(Data de Nascimento): ")  # Solicita a senha
    if senha_log == senha:
        break  # Sai do loop se estiver correto
    else:
        print("Erro: Login inválido. Tente novamente.")

exibir_nome()

