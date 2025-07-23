class ContaBancaria:

    def __init__(self, titular='', saldo=0):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False

    @property
    def ativo(self):
        return self._ativo

    @ativo.setter
    def ativo(self, valor):
        if isinstance(valor, bool):
            self._ativo = valor

    def __str__(self):
        situacao = ''
        if self.ativo == True:
            situacao = "Ativo"
        else:
            situacao = "Inativo"
        saldo_formatado = f'{self.saldo:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
        return f'Titular da Conta: {self.titular:<18} | Saldo: R${saldo_formatado:<10} | Situação: {situacao}'

    def alter_status(self):
        self.ativo = not self.ativo

class ClientesBanco: 
    
    def __init__(self, nome, idade=0, cidade, cpf, email):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.cpf = cpf
        self.email = email

    def __str__(self):
        return f'Nome: {self.nome:<18} | idade: R${self.idade:<3} | Cidade: {self.cidade:<15}, CPF: {self.cpf:<11}, E-mail: `{self.email}'

n1 = ClientesBanco("Tião", 22, "SJP", "07509688822", "tiao@gmail.com")
n2 = ClientesBanco("Gastão B", 94, "Salvador", "07509622222", "naotem@gmail.com")
m3 = ClientesBanco("Aroeiro", 50, "Desconhecido", "07509633355", "pecaquevocequeira@gmail.com")

cl1 = ContaBancaria("Tião do Gás", 10000)
cl2 = ContaBancaria("Gastão Bahiano", 1200)
cl3 = ContaBancaria("Nene dos Fetos", 20)

cl1.alter_status()

print(f'{cl1}\n{cl2}\n{cl3}')

"""
1. Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo.
Inicie o atributo ativo como False por padrão. ***OK***

2. Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada
com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias. ***OK***

3. Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo
ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.

4. Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos.
Utilize propriedades, se necessário.

5. Crie uma instância da classe e imprima o valor da propriedade titular.

6. Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos
desta classe e atribua valores aos seus atributos através do método construtor.

7. Crie um método de classe para a conta ClienteBanco."""