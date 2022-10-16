import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import lyric_finder as lf
import keys
import re

spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials(keys.spotify_id, keys.spotify_secret))


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

    lyrics = []
    playlist = spotify.playlist(id)
    all_tracks = playlist["tracks"]["items"]

    for track in all_tracks:
        artist = track["track"]["artists"][0]["name"]
        title = track["track"]["name"]
        print("Found song: " + title + " - " + artist)
        scraped_lyrics = lf.scrape_lyrics(artist, title)
        if scraped_lyrics:
            lyrics.append(scraped_lyrics)
        if len(lyrics) == 0:
            raise Exception("No lyrics found")
    return lyrics