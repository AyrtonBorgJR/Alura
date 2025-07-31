class Veiculo:
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._ligado = False

    def __str__(self):
        status = "Ligado" if self._ligado else "Desligado"
        return f'{self._marca} | {self._modelo} | {status}'

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self._portas = portas      
    
    def __str__(self):
         return f'{super().__str__()} | {self._portas} portas'

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self._tipo = tipo

    def __str__(self):
        return f'{super().__str__()} | Tipo: {self._tipo}'

carro_1 = Carro("Civic", "Honda", 4)
carro_2 = Carro("Logan", "Renault", 4)
carro_3 = Carro("Fusca", "VW", 2)

moto1 = Moto("Bis", "Yamaha", "Casual")
moto2 = Moto("Motoneta", "Desconhecida", "Espoeriva")
moto3 = Moto("Ninja", "Kawasaki", "Esportiva")

print(f'{carro_1}\n {carro_2}\n {carro_3}\n {moto1}\n {moto2}\n {moto3}')

""""
8. Importe e Instancie Objetos: No arquivo main.py, importe as classes Carro e Moto. Em seguida, crie três
instâncias de Carro e Moto com diferentes marcas, modelos, quantidade de portas e tipos.

9. Exiba as Informações: Para cada instância, imprima no console as informações utilizando o método str.
"""