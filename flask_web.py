from flask import Flask, render_template, request, flash
from components.playlist_class import MP3Playlist
from components.song_class import Song

app = Flask(__name__)

users_database = {
    "ekow" : "ekow1",
    "sackey" : "sackey1",
    "edem" : "edem1",
    "user" : "user1",
    "2high2cry" : "canidiealready123",
}

playlist = MP3Playlist()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/authorize', methods=['GET', 'POST'])
def authorize():
    
    username = request.form.get('username')
    password = request.form.get('password')
    
    if username in users_database.keys():
        if users_database[username] == password:
            return render_template('landingPage.html', username = username)
        else:
            return render_template('errorPage.html', error = "Wrong password.")
        
    else:
        return render_template('errorPage.html', error = "Username does not exist.")
        

@app.route('/logout')
def logout():
    return render_template('index.html')

@app.route('/createPlaylist', methods=['GET', 'POST'])
def create_playlist():
    return render_template('createPlaylist.html')
    
    
@app.route('/createSong', methods=['GET', 'POST'])
def new_song():
    return render_template('createSong.html') 



# def create_song(song_title, artist_name, release_year, duration, genre):
#     song = Song(song_title, artist_name, release_year, duration, genre)
#     return ""

@app.route('/load')
def songs_page():
    return render_template('songsPage.html')



# def add_song(song, name):
#     name.add_song(song)
#     return f'{song} added to playlist'

@app.route('/clear')
def clear_playlist():
    # name.clear_playlist()
    
    return "playlist cleared"

@app.route('/display')
def display():
    return render_template('display.html')



# def display_all(name):
#     name.display_all()
#     return ""

if __name__ == '__main__':
    app.run(debug= True, host= '0.0.0.0')