class Banco:
    def __init__(self, nome, endereco):
        self._nome = nome
        self._endereco = endereco

class Agencia(Banco):
    def __init__(self, nome, endereco, numero):
        super().__init__(nome, endereco)
        self._numero = numero

    def __str__(self):
        return f'{self._nome} {self._endereco} {self._numero}'

ag1 = Agencia("ABC Paulista", "Faria Lima", 22)

print(ag1)