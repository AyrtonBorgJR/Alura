class Musica:
    musicas = []
    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)

    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'

    def lista_musica():
        print(f'{"Nome":<30} | {"Artista":<20} | {"Duração":<10}')
        for sons in Musica.musicas:
            print(f'{sons.nome:<30} | {sons.artista:<20} | {sons.duracao:<10}')


nome = input("Nome da musica: ")
artista = input("Quem canta? ")
duracao = input("Duração em segundos: ")

Musica(nome, artista, duracao)

Musica.lista_musica()