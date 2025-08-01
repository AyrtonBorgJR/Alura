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
