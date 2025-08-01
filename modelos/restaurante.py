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