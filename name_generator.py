
import cohere
co = cohere.Client(api_key='PoDA0pxkWb7oyLlkLajAd5zqaRWL43U0bxNyW31L')


def get_summary(all_lyrics, model='small', max_tokens=10, 
temperature=0.8, num_generations=1, k=0, p=1): 
    compiled_summaries = '';
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



lyrics1 = '''I don't want a friend (just me)"""
I want my life in two (my life in two)
Just one more night
Waiting to get there
Waiting for you (all night)
I'm done fighting all night (waiting for you)
When I'm around slow dancing in the dark
Don't follow me, you'll end up in my arms
You have made up your mind
I don't need no more signs
Can you?
Can you?
Give me reasons we should be complete
You should be with him, I can't compete
You looked at me like I was someone else, oh well
Can't you see? (Can't you see?)
I don't wanna slow dance (I don't want to slow dance)
In the dark
Dark
When you gotta run
Just hear my voice in you (my voice in you)
Shutting me out of you (shutting me out of you)
Doing so great (so great, so great)
You
Used to be the one (used to be the one)
To hold you when you fall
Yeah, yeah, yeah (when you fall, when you fall)
I don't fuck with your tone (I don't fuck with your tone)
I don't wanna go home (I don't wanna go home)
Can it be one night?
Can you?
Can you?
Give me reasons we should be complete
You should be with him, I can't compete
You looked at me like I was someone else, oh well
Can't you see?
I don't wanna slow dance (I don't want to slow dance)
In the dark
Dark
In the dark
Dark'''

lyrics2 = '''Will you let me come closer to you
I know that you're older, but what can I do
I leave in the morning I'll forget that I am surely falling
Grew up in a case of fragile glass
But hammer away it's time to crash
And as it shatters let me shatter into you
The soft candle glow
The music so slow
Your skin on my skin
The room is spinning
Nerve in my bone
I'm shaking oh no
I'm talking though I shouldn't be
I've lost all sensibility
Ooh, I've never been so fragile
It's been a year and forty days
Since you picked me up and swept me away
I wanted to run with you into the midnight sun with you
Now I sit around and rust in rain
Turn into dust as I just wait
For someone to hold me like you did that night I still remember
The soft candle glow
The music so slow
Your skin on my skin
The room kept spinning
Round I'm alone
New town on my own
I'm missing you I shouldn't be
I've lost all sensibility
Ooh, I've never been so fragile
Fragile'''
#get_summary([lyrics1, lyrics2], num_generations=1)
