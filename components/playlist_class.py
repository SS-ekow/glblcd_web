from collections import deque
from components.song_class import Song
    
class MP3Playlist:
    def __init__(self, name):
        self.playlist = deque()
        self.name = name

    def load_playlist(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                song_details = line.strip().split(",")
                if len(song_details) == 5:
                    song = Song(*song_details)
                    self.add_song(song)

    def display_all(self):
        if not self.playlist:
            print("Your Playlist is empty.")
        else:
            print("Your Playlist:")
            for index, song in enumerate(self.playlist, start=1):
                print(f"{index}. {song}")

    def add_song(self, song):
        self.playlist.append(song)
        print(f"Added {song} to the playlist.")
        
    def clear_playlist(self):
        self.playlist.clear()
        print('You have cleared your playlist')
        
    def get_duration(self):
        durations = []
        for song in self.playlist:
            durations.append(song.duration)
            
        x = [int(i.split(':')[0]) for i in durations]
        y = [int(i.split(':')[1]) for i in durations]
        
        
        total_minutes = sum(x)
        total_seconds = sum(y)
        
        while total_seconds >= 60:
            total_minutes += 1
            total_seconds -= 60
            
    
            
        return f'Total duration of playlist: {total_minutes} mins and {total_seconds} seconds'
    
    def save_on_file(self, file_path):
        with open(file_path, 'w') as file:
            for song in self.playlist:
                file.write(f"{song.song_title},{song.artist_name},{song.release_year},{song.duration},{song.genre}\n")
                
        print(f'Playlist saved on {file_path}')
        
    # def remove_song(self, song_title):
    #     for song in self.playlist:
    #         if song.song_title == song_title:
    #             self.playlist.remove(song)
    #             print(f'{song_title} has been removed from your playlist')