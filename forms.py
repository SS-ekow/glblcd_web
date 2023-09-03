from flask_wtf import FlaskForm
from wtforms import StringField,  SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(min=1, max=40)])
    password = StringField('Password', validators=[DataRequired(), Length(min=4, max=40)])
    confirm_password = StringField('Confirm Password', validators=[DataRequired(), EqualTo('password')])  
    submit = SubmitField('Sign Up')  
    

class createPlaylistForm(FlaskForm):
    playlist_name = StringField('Playlist Name', validators=[DataRequired(), Length(min=1, max=40)])
    submit = SubmitField('Create Playlist') 
    
class createSongForm(FlaskForm):
    song_title = StringField('Song Title', validators=[DataRequired(), Length(min=1, max=40)])
    artist_name = StringField('Artist Name', validators=[DataRequired(), Length(min=1, max=40)])
    release_year = StringField('Release Year', validators=[DataRequired(), Length(min=1, max=40)])
    duration = StringField('Duration', validators=[DataRequired(), Length(min=1, max=40)])
    genre = StringField('Genre', validators=[DataRequired(), Length(min=1, max=40)])
    submit = SubmitField('Create Song')