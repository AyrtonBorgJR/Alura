from abc import ABC, abstractmethod

class Restaurante():
    """Representa um restaurante com avaliações, cardápio e status ativo/inativo."""

    estabelecimentos = []

    def __init__(self, nome, categoria):
        """
        Inicializa um novo restaurante.

        Args:
            nome (str): Nome do restaurante.
            categoria (str): Categoria do restaurante (ex.: 'Gourmet', 'Mexicano').
        """

        self._nome = nome.title() 
        self._categoria = categoria.upper() 
        self._ativo = False
        self._avaliacao = [] # Lista de avaliações recebidas
        self._cardapio = [] # Lista de itens do cardapio
        Restaurante.estabelecimentos.append(self) 

    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod 
    def lista_restaurantes(cls):
        """Exibe todos os restaurantes cadastrados no console."""
        print(f'{"Restaurante":<25} | {"Categoria":<10} | {"Avaliação":<9} | {"Status":<3}' )
        for restaurante in cls.estabelecimentos:
            print(f'{restaurante._nome:<25} | {restaurante._categoria:<10} | {restaurante.media_avaliacoes:<9} | {restaurante.ativo:<3}')

    @property
    def ativo(self):
        """Retorna um símbolo indicando se o restaurante está ativo ou não."""
        return "✓" if self._ativo else "⌧"

    def alt_status(self):
        """Alterna o status do restaurante entre ativo e inativo."""
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        """
        Adiciona uma nova avaliação para o restaurante.

        Args:
            cliente (str): Nome do cliente.
            nota (float): Nota da avaliação (0 a 10).
        """
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        """Calcula e retorna a média das avaliações ou '-' se não houver nenhuma."""
        if not self._avaliacao:
            return "-"
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        qtde_notas = len(self._avaliacao)
        media = round(soma_notas / qtde_notas,1)
        return media

    def adicionar_no_cardapio(self, item): 
        """
        Adiciona um item ao cardápio do restaurante, caso seja uma instância de ItemCardapio.
        """
        if isinstance(item, ItemCardapio): 
            self._cardapio.append(item)

    @property
    def exibir_cardapio(self):
        """Exibe todos os itens do cardápio enumerados no console."""
        print(f'Cardapio do restaurante {self._nome}\n')
        for i,item in enumerate(self._cardapio,start=1):
            if hasattr(item, '_descricao'):
                msgn_prato = f'{i}. Nome: {item._nome} | Preço: {item._preco} | Descrição: {item._descricao}'
                print(msgn_prato)
            else:
                msgn_bebida = f'{i}. Nome: {item._nome} | Preço: {item._preco} | Tamanho: {item._tamanho}'
                print(msgn_bebida)

#from modelos.restaurante import Restaurante
class Avaliacao:
    """Representa uma avaliação de um restaurante."""
    def __init__(self, cliente, nota):
        """
        Cria uma nova avaliação.

        Args:
            cliente (str): Nome do cliente que avaliou.
            nota (float): Nota da avaliação (0 a 10).
        """
        self._cliente = cliente
        self._nota = nota

#from modelos.avaliacao import Avaliacao:
class ItemCardapio(ABC): 
    """Classe base para itens do cardápio (pratos e bebidas)."""
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @abstractmethod
    def aplicar_desconto(self):
        pass

#from modelos.cardapio.item_cardapio import ItemCardapio
class Prato(ItemCardapio): 
    """Representa um prato do cardápio."""
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao

    def __str__(self):
        return self._nome

    def aplicar_desconto(self):
        self._preco = self._preco - (self._preco * 0.05)

#from modelos.cardapio.prato import Prato
class Bebida(ItemCardapio):
    """Representa uma bebida do cardápio."""
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho

    def __str__(self):
        return self._nome

    def aplicar_desconto(self):
        self._preco = self._preco - (self._preco * 0.05)


#from modelos.cardapio.bebida importe Bebida

# ============================
# Exemplo de uso
# ============================

restaurante_bom = Restaurante('praca', 'Gourmet')
restaurante_ruim = Restaurante('MexFood', 'Mexicano')
restaurante_3 = Restaurante('Japa', 'Japones')

bebida_suco = Bebida("Suco de Melancia", 9.0, "Grande")
bebida_suco.aplicar_desconto()

prato_macarrao = Prato("Bolonhesa", 35.0, "Macarrona classica da Nona")
prato_macarrao.aplicar_desconto()
restaurante_bom.adicionar_no_cardapio(bebida_suco)
restaurante_bom.adicionar_no_cardapio(prato_macarrao)


restaurante_bom.receber_avaliacao("Sebastian", 10)
restaurante_bom.receber_avaliacao("Aloi", 8)
restaurante_bom.receber_avaliacao("Jotaro", 1)

restaurante_3.alt_status()

def main():
    restaurante_bom.exibir_cardapio

if __name__ == '__main__':
    main()