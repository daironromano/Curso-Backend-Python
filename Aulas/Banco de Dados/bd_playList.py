class Musica:
    def __init__(self, titulo, artista, duracao):
        self.titulo = titulo
        self.artista = artista
        self.duracao = duracao

    #Método especial para o desenvolvedor
    def __repr__(self):
        return f"Música: (titulo={self.titulo}), artista={self.artista}, duracao={self.duracao}"

    #Método especial para o usuário
    def __str__(self):
        return f"Título: {self.titulo}\nDuração: {self.duracao}"

class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self._musicas = []

    def __str__(self):
        pass
    def __repr__(self):
        pass
    def __len__(self):
        pass
    def __getitem__(self):
        pass

musica1 = Musica('Vai malandra', 'Anitta', '2:30')
print(musica1)