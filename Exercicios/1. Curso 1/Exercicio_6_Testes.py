import os

clientes = [{'nome': 'Catiço', 'categoria':'Viadão', 'idade':'240'},
           {'nome': 'Carniça', 'categoria':'Trans', 'idade':'28'},
           {'nome': 'Troço', 'categoria':'Bicha', 'idade':'22'}]

restaurantes = [{'nome':'Restaurante Pai e mãe', "categoria":"Brasileiro", "ativo":False},
                {'nome':'Pizzaiolo', "categoria":"Pizza", "ativo":False},
                {'nome':'Rosca Sushi', "categoria":"Japones", "ativo":True}]

def main():
    os.system('clear')
    exibir_opcoes()
    escolher_opcao()

def opcao_invalida():
    print("Opção Invalida!\n")
    voltar_ao_menu_principal()

def exibir_opcoes():
    print("Menu de Opções:")
    print("1. Nova Chave")
    print("2. Deletar Chave")
    print("3. Qaudrados")
    print("4. Dicionário")
    print("5. Sair\n")

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Selecione: ")) 
        print(f"Você escolheu a opção {opcao_escolhida}")

        if opcao_escolhida == 1:
            nova_chave()
        elif opcao_escolhida == 2:
            del_chave()
        elif opcao_escolhida == 3:
            quads()
        elif opcao_escolhida == 4:
            dicionario()
    except:
        opcao_invalida()

def nova_chave():
    chave = input("Digite o nome da chave: ")
    print("Restaurantes disponíveis:")
    for i, r in enumerate(restaurantes):
        print(f"{i} - {r['nome']}")
    try:
        cod = int(input("Escolha o restaurante: "))
    except ValueError:
        print("Digite um número válido!")
        return
    
    if 0 <= cod < len(restaurantes):
        restaurantes[cod][chave] = input("Descreva: ")
        print(restaurantes)
    else:
        print("Código inválido!")
    voltar_ao_menu_principal()

def quads():
    quadrados = {}

    for numero in range(1, 6):
        quadrados[numero] = numero ** 2

    print(quadrados)

def del_chave():
    chave = input("Digite o nome da chave: ")
    cod = int(input("Escolha o restaurante: "))
    del restaurantes[cod][chave]
    print(restaurantes)

def dicionario():
    chave = input("Qual chave você deseja consultar? ")
    for restaurante in restaurantes:
        if chave in restaurante:
            print("A chave existe!")
            return
    print("Chave inexistente")

if __name__ == '__main__':
    main()

