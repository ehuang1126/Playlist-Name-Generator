
import cohere
import keys

co = cohere.Client(api_key=keys.cohere)


def get_summary(all_lyrics, model='small', max_tokens=10, 
temperature=0.8, num_generations=1, k=0, p=1): 
    compiled_summaries = ''
    for lyric in all_lyrics: 
        compiled_summaries += co.generate(
            model='small',
            prompt=lyric,
            max_tokens=5,
            temperature=temperature,
            num_generations=1,
            k=k,
            p=p
        ).generations[0].text.replace('\n', ' ')
    response = co.generate(
        model='small',
            prompt=compiled_summaries,
            max_tokens=max_tokens,
            temperature=temperature,
            num_generations=num_generations,
            k=k,
            p=p
    )
    for i in range(num_generations): 
        print(response.generations[i].text)

def get_summary_simple(compiled_lyrics, model='large', max_tokens=10, 
temperature=0.8, num_generations=1, k=0, p=1): 
    response = co.generate(
        model=model,
        prompt=compiled_lyrics,
        max_tokens=max_tokens,
        temperature=temperature,
        num_generations=num_generations,
        k=k,
        p=p
    )
    for i in range(num_generations): 
        print(response.generations[i].text)