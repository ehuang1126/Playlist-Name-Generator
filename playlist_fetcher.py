import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import lyric_finder as lf
import re

#TODO: ========================= DELETE THESE KEYS WHEN SUBMITTING ============================

my_id = "10fc7a6976ad4a759bfacb6d565a6198"
my_secret = "11c4bb638fc44c7eb17542e64e735eb2"
my_uri = "https://localhost:8888/callback"

#TODO: =========================================================================================

#test_url = "https://open.spotify.com/playlist/3DFrt1FvEhWt3ZvyhyD9Z5?si=d3ec0f0906bc48c2"
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(my_id, my_secret))


def getAllLyrics(id):
    #if re.match("[https://open.spotify.com/playlist/]", playlist_id):


    lyrics = ""
    playlist = spotify.playlist(id)
    all_tracks = playlist["tracks"]["items"]

    for track in all_tracks:
        artist = track["track"]["artists"][0]["name"]
        title = track["track"]["name"]
        lyrics += lf.scrape_lyrics(artist, title) + "\n"
    return lyrics


def getSongLyrics(artist, title):
    #helper to return lyrics of song specified by artist and title
    #currently returns parameters as a default test
    return artist + " - " + title


print(getAllLyrics("3DFrt1FvEhWt3ZvyhyD9Z5"))