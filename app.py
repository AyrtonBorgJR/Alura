import os

clientes = [{'nome': 'Catiço', 'categoria':'Viadão', 'idade':'240'},
           {'nome': 'Carniça', 'categoria':'Trans', 'idade':'28'},
           {'nome': 'Troço', 'categoria':'Bicha', 'idade':'22'}]

restaurantes = [{'nome':'Restaurante Pai e mãe', "categoria":"Brasileiro", "ativo":False},
                {'nome':'Pizzaiolo', "categoria":"Pizza", "ativo":False},
                {'nome':'Rosca Sushi', "categoria":"Japones", "ativo":True}]



def exibir_nome():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")

def voltar_ao_menu_principal():
    
    input("\nDigite uma tecla para voltar ao menu inicial ")
    main()

def exibir_subtitulo(texto):
    os.system("clear")
    lin = '*' * (len(texto) + 4)
    print(f"{lin}\n{texto}\n{lin}")
    print("")

def exibir_opcoes():
    print("Menu de Opções:")
    print("1. Cadastro de Restaurante")
    print("2. Listar Restaurante")
    print("3. Ativar Restaurante")
    print("4. Cadastro de Clientes")
    print("5. Listar Clientes")
    print("6. Sair\n")

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Selecione: ")) 
        print(f"Você escolheu a opção {opcao_escolhida}")
        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurante()
        elif opcao_escolhida == 3:
            ativar_restaurante()
        elif opcao_escolhida == 4:
            cadastrar_clientes()
        elif opcao_escolhida == 5:
            listar_clientes()
        elif opcao_escolhida == 6:
            encerrar_programa()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def cadastrar_restaurante():
    caminho = input("Oque deseja?\n 1. Novo Cadastro\n 2. Alterar Cadastro")
    
    if caminho == "1":
        exibir_subtitulo('Cadastrar restaurantes')
        nome_rest = input('Digite o nome do restaurante que deseja cadastrar: ')
        categoria = input(f'Digite a categoria do restaurante {nome_rest}: ')
        dados = {'nome':nome_rest, "categoria":categoria, 'ativo':False}
    
        restaurantes.append(dados)
        print(f'O restaurante {nome_rest} foi cadastrado com sucesso')
        voltar_ao_menu_principal()

    if caminho == "2":
        print("Qual restaurante você deseja alterar:")
        print(f"{'Cod':<5} | {'Nome':<10} | {'Categoria':<10}")
        for idx, restaurante in enumerate(restaurantes, start=1):
            print(f"{idx:<5} | {restaurante['nome']:<10} | {restaurante['categoria']:<10}")

    codigo = int(input("\nDigite o código do restaurante: ")) - 1

    if 0 <= codigo < len(restaurantes):
        print("\nDeseja alterar o quê?")
        print("1. Nome\n2. Categoria\n")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            restaurantes[codigo]['nome'] = input("Novo nome: ")
        elif opcao == '2':
            restaurantes[codigo]['categoria'] = input("Nova categoria: ")
        else:
            print("Opção inválida.")
    else:
        print("Código inválido.")

    print("\nRestaurantes atualizados:")
    print(f"{'Cod':<5} | {'Nome':<10} | {'Categoria':<10}")
    for idx, restaurante in enumerate(restaurantes, start=1):
        print(f"{idx:<5} | {restaurante['nome']:<10} | {restaurante['categoria']:<10}")
    voltar_ao_menu_principal()
            
def listar_restaurante():
    exibir_subtitulo('Listando os restaurantes: ')
    print(f'{"ESTABELECIMENTO".ljust(30)} | {"CATEGORIA".ljust(28)} | {"STATUS"}')
    for restaurante in restaurantes:
        ativo = "Ativado" if restaurante["ativo"] else "Inoperante"
        print(f"* {restaurante['nome'].ljust(28)} | {restaurante['categoria'].ljust(28)} | {ativo}")

    voltar_ao_menu_principal()

def ativar_restaurante():
    exibir_subtitulo('Alterar estado do restaurante')
    identificacao_restaurante = input("Digite o nome do restaurante que você deseja alterar o estado: ")
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if identificacao_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante["ativo"]
            msg = f'O restaurante {identificacao_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante {identificacao_restaurante} foi desativado com sucesso'
            print(msg)
    if not restaurante_encontrado:
        print("Restaurante não encontrado")
    voltar_ao_menu_principal()

def cadastrar_clientes():
    exibir_subtitulo('Cadastrar clientes')
    nome_cli = input('Digite o nome do cliente que deseja cadastrar: ')
    categoria = input(f'Digite a categoria do cliente {nome_cli}: ')
    idade = input(f'Digite a idade do cliente: ')
    dados = {'nome':nome_cli, "categoria":categoria, 'idade':idade}
    
    clientes.append(dados)
    print(f'O restaurante {nome_cli} foi cadastrado com sucesso')
    voltar_ao_menu_principal()

def listar_clientes():
    exibir_subtitulo('Listando Clientes: ')
    print(f'{"CLIENTE".ljust(30)} | {"CATEGORIA".ljust(28)} | {"IDADE"}')
    for cliente in clientes:
        print(f"* {cliente['nome'].ljust(28)} | {cliente['categoria'].ljust(28)} | {cliente['idade']}")
              
    voltar_ao_menu_principal()

def encerrar_programa():
    exibir_subtitulo('Finalizando o app')

def opcao_invalida():
    print("Opção Invalida!\n")
    voltar_ao_menu_principal()

def main():
    os.system('clear')
    exibir_nome()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()