class pessoa:
    def __init__(self, nome="", idade=0, profissao=""):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'{self.nome}, {self.idade}, {self.profissao}'

    def aniversario(self):
        self.idade = self.idade + 1
    
    @property
    def saudacao(self):
        return f'Ola {self.nome} parabens pelo dia do {self.profissao} comemorando com {self.idade} anos'


nome = input("Nome:" )
idade = int(input("Qtos anos? "))
profissao = input("Profissão")

infeliz = pessoa(nome, idade, profissao)
infeliz.aniversario()
print(infeliz.saudacao)

""""Crie uma nova classe chamada Pessoa com atributos como nome, idade e profissão.
    Adicione um método especial __str__ para imprimir uma representação em string da pessoa.
    Implemente também um método de instância chamado aniversario que aumenta a idade da pessoa em um ano.
    Por fim, adicione uma propriedade chamada saudacao que retorna uma mensagem de 
    saudação personalizada com base na profissão da pessoa."""