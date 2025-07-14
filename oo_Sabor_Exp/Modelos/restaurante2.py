class Restaurante():
    estabelecimentos = []

    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.estabelecimentos.append(self)
    def __str__(self):
        return f'{self.nome} | {self.categoria}'

    def lista_restaurantes():
        for restaurante in Restaurante.estabelecimentos:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')

 
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Express', 'Pizzaria')

Restaurante.lista_restaurantes()