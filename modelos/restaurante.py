class Avaliacao:
    def __init__(self, cliente, nota):
    self._cliente = cliente
    self._nota = nota

"""from modelos.avaliacao import Avaliacao:"""

class Restaurante():
    estabelecimentos = []

    def __init__(self, nome, categoria):
        self._nome = nome.title() #Titulo
        self._categoria = categoria.upper() #Tudo em MAIUSCULO
        self._ativo = False
        self._avaliacao = []
        Restaurante.estabelecimentos.append(self)

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def lista_restaurantes(cls):
        print(f'{"Restaurante":<25} | {"Categoria":<10} | {"Status":<6}' )
        for restaurante in cls.estabelecimentos:
            print(f'{restaurante._nome:<25} | {restaurante._categoria:<10} | {restaurante.ativo:<6}')

    @property
    def ativo(self):
        return "✓" if self._ativo else "⌧"

    def alt_status(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

