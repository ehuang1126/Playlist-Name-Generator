from bs4 import BeautifulSoup
import requests
import re

def scrape_lyrics(artist, title):
    artist = artist.replace(' ', '-') if ' ' in artist else str(artist)
    title = title.replace(' ', '-') if ' ' in title else str(title)

    page = requests.get(f'https://genius.com/{artist}-{title}-lyrics')
    html = BeautifulSoup(page.text, 'html.parser')
    lyrics = html.find('div', class_='lyrics')
    if not lyrics: 
        lyrics = html.find('div', class_='Lyrics__Container-sc-1ynbvzw-6')
    if not lyrics: 
        return ""

    lyric_text = lyrics.get_text(' ').replace('Chorus', '')
    lyric_text = lyric_text.replace('Verse', '')
    lyric_text = lyric_text.replace('Pre-Chorus', '')
    lyric_text = lyric_text.replace('[', '')
    lyric_text = lyric_text.replace(']', '')
    return lyric_text