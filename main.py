import playlist_fetcher
import name_generator
import lyric_finder

def get_playlist_name(playlist_url, model='large', max_tokens=10, 
temperature=0.8, num_generations=1, k=0, p=1):
    name_generator.get_summary(playlist_fetcher.get_all_lyrics(playlist_url), model=model, 
                               max_tokens=max_tokens, temperature=temperature, 
                               num_generations=num_generations, k=k, p=p)

def main(): 
    get_playlist_name('https://open.spotify.com/playlist/37i9dQZF1DZ06evO4iRboc?si=0a690d83ceb54fdc', model='large', max_tokens=5)

if __name__ == "__main__": 
    main()