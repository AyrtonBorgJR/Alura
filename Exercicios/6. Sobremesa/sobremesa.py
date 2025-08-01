from abc import ABC, abstractmethod

class ItemCardapio(ABC): 
    """Classe base para itens do cardápio (pratos e bebidas)."""
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @abstractmethod
    def aplicar_desconto(self):
        pass

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tipo, tamanho, descricao):
        super().__init__(nome, preco)
        self._tipo = tipo
        self._tamanho = tamanho
        self._descricao = descricao

    def aplicar_desconto(self):
        self._preco = self._preco - (self._preco * 0.05)

    def __str__(self):
        return f'{self._nome} | {self._preco} | {self._tipo} | {self._tamanho} | {self._descricao}'

sorvete = Sobremesa("Baunilha", 40, "Gelato", "Grande", "Sorvete de baulinha derretido")
sorvete.aplicar_desconto()

print(sorvete)

"""
1. Crie uma classe chamada Sobremesa que herda de ItemCardapio, adicione atributos específicos
como tipo, tamanho e descricao à classe Sobremesa. Ajuste a inicialização da classe para incluir
esses novos atributos, possibilitando a criação de um novo item ao cardápio do restaurante.

2. Atualize o método __str__ conforme necessário para refletir essas mudanças.

3. Certifique-se de que a classe Sobremesa mantenha a herança do método aplicar_desconto de ItemCardapio.

"""

