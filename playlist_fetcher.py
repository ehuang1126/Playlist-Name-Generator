import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import lyric_finder as lf
import keys
import re

test_url = "https://open.spotify.com/playlist/3DFrt1FvEhWt3ZvyhyD9Z5?si=d3ec0f0906bc48c2"
spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(keys.id, keys.secret))


def get_all_lyrics(playlist_link):
    """Returns a string containing all the lyrics of the songs in a playlist specified by playlist_link (a playlist ID, URL, or URI)."""

    if re.fullmatch("https:\/\/open\.spotify\.com\/playlist\/(\w{22}).*", playlist_link):
        id = playlist_link[34:56]
    elif re.fullmatch("(\w{22})", playlist_link):
        id = playlist_link
    elif re.fullmatch("spotify:track:(\w{22})", playlist_link):
        id = playlist_link[14:36]
    else:
        raise Exception("Malformed playlist link/id")

    lyrics = ""
    playlist = spotify.playlist(id)
    all_tracks = playlist["tracks"]["items"]

    for track in all_tracks:
        artist = track["track"]["artists"][0]["name"]
        title = track["track"]["name"]
        lyrics += lf.scrape_lyrics(artist, title) + "\n"
    return lyrics

print(get_all_lyrics(test_url))