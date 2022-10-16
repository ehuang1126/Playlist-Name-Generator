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
        return None

    

    return lyrics.get_text(' ')


print(scrape_lyrics('Joji', 'Slow Dancing in the Dark'))