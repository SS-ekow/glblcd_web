from flask import Flask, render_template, request, flash, url_for, redirect
from components.playlist_class import MP3Playlist
from components.song_class import Song
from forms import RegistrationForm, createPlaylistForm, createSongForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '55af5c09aad400be122a'

users_database = {
    "ekow" : "ekow1",
    "sackey" : "sackey1",
    "edem" : "edem1",
    "user" : "user1",
    "2high2cry" : "canidiealready123",
}

# playlist = MP3Playlist(name= )

@app.route('/')
@app.route('/home')
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
       
        
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        users_database[form.username.data] = form.password.data
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)


@app.route('/logout')
def logout():
    return render_template('index.html')

@app.route('/createPlaylist', methods=['GET', 'POST'])
def create_playlist():
    playlist_form = createPlaylistForm()
    return render_template('createPlaylist.html')
    
    
@app.route('/createSong', methods=['GET', 'POST'])
def new_song():
    return render_template('createSong.html') 




@app.route('/load')
def songs_page():
    return render_template('songsPage.html')





@app.route('/clear')
def clear_playlist():
    # name.clear_playlist()
    
    return "playlist cleared"

@app.route('/display')
def display():
    return render_template('display.html')



if __name__ == '__main__':
    app.run(debug= True, host= '0.0.0.0')