# Playlist Name Generator

Is your favorite playlist lacking a creative title? We feel that in this modern age of digital music, far too many people suffer from this problem of uninspiring, uncreative playlist titles (us included). That’s why, with the help of Cohere’s textual summarization features, we’ve created a tool to solve this problem. Taking a Spotify playlist, we fetch the lyrics of each song off Genius and use Cohere’s pre-trained model to generate a short, unique title that captures the essence of the songs within it. Now, you can create your own abstract and emotional playlist titles without having to go through the struggle of creating it yourself. Developed for CalHacks 9.0

# Requirements

This program relies on the APIs from Spotify and Cohere. Please put their developer keys into a file called keys.py with the format:
spotify_id = "SPOTIFY-CLIENT-ID"
spotify_secret = "SPOTIFY-SECRET-ID"
cohere = "COHERE-API-KEY"

Dependencies:
cohere 2.6.1
beautifulsoup4 4.10.0
requests 2.26.1
spotipy 2.20.0