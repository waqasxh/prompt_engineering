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
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message.content


def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message.content


def chat1():
    messages =  [  
    {'role':'system', 'content':'You are an assistant that speaks like Shakespeare.'},    
    {'role':'user', 'content':'tell me a joke'},   
    {'role':'assistant', 'content':'Why did the chicken cross the road'},   
    {'role':'user', 'content':'I don\'t know'}  ]

    response = get_completion_from_messages(messages, temperature=1)
    print(response)


def chat2():
    messages =  [  
    {'role':'system', 'content':'You are friendly chatbot.'},    
    {'role':'user', 'content':'Hi, my name is Isa'}  ]
    response = get_completion_from_messages(messages, temperature=1)
    print(response)


def chat3():
    messages =  [  
    {'role':'system', 'content':'You are friendly chatbot.'},    
    {'role':'user', 'content':'Yes,  can you remind me, What is my name?'}  ]
    response = get_completion_from_messages(messages, temperature=1)
    print(response)


def chat4():
    messages =  [  
    {'role':'system', 'content':'You are friendly chatbot.'},
    {'role':'user', 'content':'Hi, my name is Isa'},
    {'role':'assistant', 'content': "Hi Isa! It's nice to meet you. \
    Is there anything I can help you with today?"},
    {'role':'user', 'content':'Yes, you can remind me, What is my name?'}  ]
    response = get_completion_from_messages(messages, temperature=1)
    print(response)


def main():
    #chat1()
    #chat2()
    #chat3()
    chat4()
        
    
if __name__ == "__main__":
    main()