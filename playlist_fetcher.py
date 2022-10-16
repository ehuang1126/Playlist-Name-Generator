import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = "10fc7a6976ad4a759bfacb6d565a6198"
client_secret = "11c4bb638fc44c7eb17542e64e735eb2"

help_url = "https://open.spotify.com/playlist/5S5QKvTZDKjMjN1M4rauyw?si=b6f9ce9ad5564c24"
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())




def getPlaylist(url):
    playlist = spotify.playlist(url)
    for track in playlist:
        #getLyrics(track)
        print(track)
    

def getLyrics(track):
    return

getPlaylist("5S5QKvTZDKjMjN1M4rauyw")