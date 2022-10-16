
import cohere
co = cohere.Client(api_key='PoDA0pxkWb7oyLlkLajAd5zqaRWL43U0bxNyW31L')


"""response = co.generate(prompt='Once upon a time in a magical land called')

print('Prediction: {}'.format(response.generations[0].text))"""

def get_summary(compiled_lyrics): 
    response = co.generate(
        model='large',
        prompt=compiled_lyrics,
        max_tokens=10,
        temperature=0.8,
        num_generations=1,
        k=0,
        p=1
    )
    print(response.generations[0].text)

get_summary("I like to eat pie")
