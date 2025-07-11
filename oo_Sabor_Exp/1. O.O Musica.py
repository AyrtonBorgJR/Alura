class Musica:
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

nome = input("Nome da musica: ")
artista = input("Quem canta? ")
duracao = input("Duração em segundos: ")

nova = Musica(nome, artista, duracao)

print(vars(musica1, musica2, musica3))
