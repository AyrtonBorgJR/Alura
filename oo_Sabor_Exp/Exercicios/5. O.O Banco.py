class ContaBancaria:

    def __init__(self, titular='', saldo=0):
        self.nome = titular
        self.saldo = saldo
        self.ativo = False

    def __str__(self):
        situacao = ''
        if self.ativo == True:
            situacao = "Ativo"
        else:
            situacao = "Inativo"
        saldo_formatado = f'{self.saldo:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
        return f'Titular da Conta: {self.nome:<18} | Saldo: R${saldo_formatado:<10} | Situação: {situacao}'

    @classmethod
    def atv_dstv_conta(self, conta):
        conta.ativo = not conta.ativo

cl1 = ContaBancaria("Tião do Gás", 10000)
cl2 = ContaBancaria("Gastão Bahiano", 1200)

ContaBancaria.atv_dstv_conta(cl2)

print(f'{cl1}\n{cl2}')

"""
1. Crie uma classe chamada ContaBancaria com um construtor que aceita os parâmetros titular e saldo.
Inicie o atributo ativo como False por padrão.

2. Na classe ContaBancaria, adicione um método especial __str__ que retorna uma mensagem formatada
com o titular e o saldo da conta. Crie duas instâncias da classe e imprima essas instâncias.

3. Adicione um método de classe chamado ativar_conta à classe ContaBancaria que define o atributo
ativo como True. Crie uma instância da classe, chame o método de classe e imprima o valor de ativo.

4. Refatore a classe ContaBancaria para utilizar a abordagem "pythonica" na criação de atributos.
Utilize propriedades, se necessário.

5. Crie uma instância da classe e imprima o valor da propriedade titular.

6. Crie uma classe chamada ClienteBanco com um construtor que aceita 5 atributos. Instancie 3 objetos
desta classe e atribua valores aos seus atributos através do método construtor.

7. Crie um método de classe para a conta ClienteBanco."""