class Song:

    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        cls.add_to_genre_count(genre)
        if cls.genres.count(genre) < 1:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        cls.add_to_artist_count(artist)
        if cls.artists.count(artist) < 1:
            cls.artists.append(artist) 

    @classmethod
    def add_to_genre_count(cls, genre):
        if cls.genre_count.get(genre) is None:
            cls.genre_count.update({genre: 1})
        else:
            cls.genre_count.update({genre: cls.genre_count[genre] + 1})
        
    @classmethod
    def add_to_artist_count(cls, artist):
        if cls.artist_count.get(artist) is None:
            cls.artist_count.update({artist: 1})
        else:
            cls.artist_count.update({artist: cls.artist_count[artist] + 1})
         