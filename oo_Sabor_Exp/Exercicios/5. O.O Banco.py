import re

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

    @classmethod
    def ativar_conta(cls, conta):
        conta.ativo = True

class ClientesBanco: 
    contador = 0
    
    def __init__(self, nome, cidade, cpf, email, idade=0):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.cpf = self.formatar_cpf(cpf)
        self.email = email

        ClientesBanco.contador += 1

    def formatar_cpf(self, cpf):
        # Remove tudo que não é dígito
        numeros = re.sub(r'\D', '', cpf)
        if len(numeros) == 11:
            return f'{numeros[:3]}.{numeros[3:6]}.{numeros[6:9]}-{numeros[9:]}'
        return 'CPF inválido'

    def __str__(self):
        return f'Nome: {self.nome:<10} | idade: {self.idade:<3} | Cidade: {self.cidade:<13}, CPF: {self.cpf:<11}, E-mail: {self.email}'

    @classmethod
    def total_clientes(cls):
        return cls.contador

n1 = ClientesBanco("Tião", "SJP", "07509688822", "tiao@gmail.com", 22)
n2 = ClientesBanco("Gastão B", "Salvador", "07509622222", "naotem@gmail.com", 90)
n3 = ClientesBanco("Aroeiro", "Desconhecido", "07509633355", "pecaquevocequeira@gmail.com", 20)

cl1 = ContaBancaria("Tião do Gás", 10000)
cl2 = ContaBancaria("Gastão Bahiano", 1200)
cl3 = ContaBancaria("Nene dos Fetos", 20)

ContaBancaria.ativar_conta(cl1)

print(f'{cl1}\n{cl2}\n{cl3}')
print(f'{n1}\n{n2}\n{n3}')
print(f"Total de clientes criados: {ClientesBanco.total_clientes()}")