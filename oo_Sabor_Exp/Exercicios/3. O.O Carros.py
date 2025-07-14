"""
1. Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. 
Crie uma instância dessa classe e atribua valores aos seus atributos.
"""
class Carro():
    lista_carro = []

    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = 0
        Carro.lista_carro.append(self)
    def __str__(self):
        return f'{self.modelo} | {self.cor} | {self.ano}'

    def modelos():
        for carro in Carro.lista_carro:
            print(f'{carro.modelo} | {carro.cor} | {carro.ano}')

carro1 = Carro("Logan", "Branco", 2014)

Carro.modelos()

"""2. Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos.
Instancie um restaurante e atribua valores aos seus atributos.

3. Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros
e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.

4. Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância,
seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma
instância de restaurante."""

class Restaurante():
    estabelecimentos = []

    def __init__(self, nome, categoria, ativo, avaliacao, bairro):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.avaliacao = avaliacao
        self.bairro = bairro
        Restaurante.estabelecimentos.append(self)
    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo} | {self.avaliacao} | {self.bairro}'

    def listar_restaurantes():
        for restaurante in Restaurante.estabelecimentos:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo} | {restaurante.avaliacao} | {restaurante.bairro}')

nome = input("Insira o nome do restaurante: ")
categoria = input("Tipo do restaurante: ")
ativo = input("Restaurante ativo? \n 1.Sim\n 2.Não")
if ativo == "1":
    ativo = True
elif ativo == "2":
    ativo = False
avaliacao = input("Avaliacao no google: ")
bairro = input("Digite o Bairro: ")

r1 = Restaurante(nome, categoria, ativo, avaliacao, bairro)

Restaurante.listar_restaurantes()

"""5. Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos
desta classe e atribua valores aos seus atributos através de um método construtor."""

class cliente():
    lista_clientes = []

    def __init__(self, nome, idade, bairro, perfil):
        self.nome = nome
        self.idade = idade
        self.bairro = bairro
        self.perfil = perfil
        cliente.lista_clientes.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.idade} | {self.bairro} | {self.perfil}'

    def listagem():
        print(f'{"Nome":<15} | {"Idade":<15} | {"Bairro":<20} | {"Perfil":<15}')
        for pessoas in cliente.lista_clientes:
            print(f'{pessoas.nome:<15} | {pessoas.idade:<15} | {pessoas.bairro:<20} | {pessoas.perfil:<15}')


nome = "Antonio"
idade = "81"
bairro = "Silveira da Motta"
perfil = "Consumidor Médio"

cliente1 = cliente(nome, idade, bairro, perfil)

cliente.listagem()