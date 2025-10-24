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

    def adicionar_musica(self, musica: Musica):
        self._musicas.append(musica)
        print(f'Música {musica.titulo} adicionada à playlist {self.nome}')

    def __repr__(self):
        return f"Playlist (nome={self.nome}, {self._musicas})"
    
    def __str__(self):
        total_musicas = len(self._musicas)
        return f"Playslist: {self.nome}\nQtde de músicas: {total_musicas}"
    
    def __len__(self):
        return len(self._musicas)

    def __getitem__(self, index):
        return self._musicas[index]
    
    def __add__(self, other):
        if not isinstance(other, Playlist):
            return NotImplemented # Indica que não é possível somar
        
        #criando nova playlist
        novo_nome = f"Mix: {self.nome} + {other.nome}"
        nova_playlist = Playlist(novo_nome)

        #adicionar músicas
        for musicas in self._musicas:
            nova_playlist._musicas.append(musicas)

        for outra_musica in other:
            nova_playlist._musicas.append(outra_musica)


musica1 = Musica('Vai malandra', 'Anitta', '2:30')
print(musica1)