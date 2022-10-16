
import cohere
co = cohere.Client(api_key='PoDA0pxkWb7oyLlkLajAd5zqaRWL43U0bxNyW31L')


"""response = co.generate(prompt='Once upon a time in a magical land called')

print('Prediction: {}'.format(response.generations[0].text))"""

def get_summary(compiled_lyrics, model='large', max_tokens=10, 
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

get_summary("I like to eat pie", num_generations=2)
