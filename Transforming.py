import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())


api_key = os.getenv('OPENAI_API_KEY_GENERIC')
client = openai.OpenAI(api_key=api_key)


def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content


def example_1():
    prompt_1 = f"""
    Translate the following English text to Spanish: \
    ```Hi, I would like to order a blender```
    """
    prompt_2 = f"""
    Tell me which language this is: 
    ```Combien coûte le lampadaire?```
    """
    prompt_3 = f"""
    Translate the following  text to French and Spanish
    and English pirate: \
    ```I want to order a basketball```
    """
    prompt_4 = f"""
    Translate the following text to Spanish in both the \
    formal and informal forms: 
    'Would you like to order a pillow?'
    """

    response_1 = get_completion(prompt_1)
    print("Completion for prompt 1:")
    print(response_1)

    response_2 = get_completion(prompt_2)
    print("Completion for prompt 2:")
    print(response_2)

    response_3 = get_completion(prompt_3)
    print("Completion for prompt 3:")
    print(response_3)

    response_4 = get_completion(prompt_4)
    print("Completion for prompt 4:")
    print(response_4)


user_messages = [
  "La performance du système est plus lente que d'habitude.",  # System performance is slower than normal         
  "Mi monitor tiene píxeles que no se iluminan.",              # My monitor has pixels that are not lighting
  "Il mio mouse non funziona",                                 # My mouse is not working
  "Mój klawisz Ctrl jest zepsuty",                             # My keyboard has a broken control key
  "我的屏幕在闪烁"                                               # My screen is flashing
] 


def example_2():
    for issue in user_messages:
        prompt = f"Tell me what language this is: ```{issue}```"
        lang = get_completion(prompt)
        print(f"Original message ({lang}): {issue}")

        prompt = f"""
        Translate the following  text to English \
        and Korean: ```{issue}```
        """
        response = get_completion(prompt)
        print(response, "\n")


def example_3():
    prompt = f"""
    Translate the following from slang to a business letter: 
    'Dude, This is Joe, check out this spec on this standing lamp.'
    """
    response = get_completion(prompt)
    print(response)


def example_4():
    data_json = { "resturant employees" :[ 
    {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},
    {"name":"Bob", "email":"bob32@gmail.com"},
    {"name":"Jai", "email":"jai87@gmail.com"}
    ]}

    prompt = f"""
    Translate the following python dictionary from JSON to an HTML \
    table with column headers and title: {data_json}
    """
    response = get_completion(prompt)
    print(response)


def spell_check1():
    text = [ 
    "The girl with the black and white puppies have a ball.",
    "Yolanda has her notebook.",
    "Its going to be a long day. Does the car need it’s oil changed?",
    "Their goes my freedom. There going to bring they’re suitcases.", 
    "Your going to need you’re notebook.", 
    "That medicine effects my ability to sleep. Have you heard of the butterfly affect?",
    "This phrase is to cherck chatGPT for speling abilitty" 
    ]
    for t in text:
        prompt = f"""Proofread and correct the following text
        and rewrite the corrected version. If you don't find
        and errors, just say "No errors found". Don't use 
        any punctuation around the text:
        ```{t}```"""
        response = get_completion(prompt)
        print(response)


text = f"""
Got this for my daughter for her birthday cuz she keeps taking \
mine from my room.  Yes, adults also like pandas too.  She takes \
it everywhere with her, and it's super soft and cute.  One of the \
ears is a bit lower than the other, and I don't think that was \
designed to be asymmetrical. It's a bit small for what I paid for it \
though. I think there might be other options that are bigger for \
the same price.  It arrived a day earlier than expected, so I got \
to play with it myself before I gave it to my daughter.
"""   


def spell_check2():    
    prompt = f"proofread and correct this review: ```{text}```"
    response = get_completion(prompt)
    print(response)

    
def spell_check3():
    prompt = f"""
    proofread and correct this review. Make it more compelling. 
    Ensure it follows APA style guide and targets an advanced reader. 
    Output in markdown format.
    Text: ```{text}```
    """
    response = get_completion(prompt)
    print(response)


def main():
    #example_1()
    #example_2()
    #example_3()
    #example_4()
    #spell_check1()
    #spell_check2()
    spell_check3()

 
if __name__ == "__main__":
    main()