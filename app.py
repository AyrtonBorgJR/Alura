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
        print(f'{"Restaurante":<25} | {"Categoria":<10} | {"Avaliação":<9} | {"Status":<3}' )
        for restaurante in cls.estabelecimentos:
            print(f'{restaurante._nome:<25} | {restaurante._categoria:<10} | {restaurante.media_avaliacoes:<9} | {restaurante.ativo:<3}')

    @property
    def ativo(self):
        return "✓" if self._ativo else "⌧"

    def alt_status(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return "-"
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qtde_notas = len(self._avaliacao)
        media = round(soma_notas / qtde_notas,1)
        return media
"""from modelos.restaurante import Restaurante"""
class Avaliacao:
    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = nota
"""from modelos.avaliacao import Avaliacao:"""

restaurante_bom = Restaurante('praca', 'Gourmet')
restaurante_ruim = Restaurante('MexFood', 'Mexicano')
restaurante_3 = Restaurante('Japa', 'Japones')

restaurante_bom.receber_avaliacao("mamek", 10)
restaurante_bom.receber_avaliacao("Aloi", 8)
restaurante_bom.receber_avaliacao("Ogai", 1)

restaurante_3.alt_status()

def main():
    Restaurante.lista_restaurantes()

if __name__ == '__main__':
    main()