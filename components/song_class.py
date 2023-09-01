class Song:
    def __init__(self, song_title, artist_name, release_year, duration, genre):
        self.song_title = song_title
        self.artist_name = artist_name
        self.release_year = release_year
        self.duration = duration
        self.genre = genre
        
    def __str__(self):
        return f"'{self.song_title}' by {self.artist_name}, {self.release_year} ({self.genre})" 