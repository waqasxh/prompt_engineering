import openai
import os
import gradio as gr
from redlines import Redlines
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


text = """
Got this for my daughter for her birthday cuz she keeps taking \
mine from my room.  Yes, adults also like pandas too.  She takes \
it everywhere with her, and it's super soft and cute.  One of the \
ears is a bit lower than the other, and I don't think that was \
designed to be asymmetrical. It's a bit small for what I paid for it \
though. I think there might be other options that are bigger for \
the same price.  It arrived a day earlier than expected, so I got \
to play with it myself before I gave it to my daughter.
"""


def spell_check2(text):    
    prompt = f"proofread and correct this review: ```{text}```"
    response = get_completion(prompt)
    diff = Redlines(text, response)
    return diff.output_markdown


def spell_check3(text):
    prompt = f"""
    proofread and correct this review. Make it more compelling. 
    Ensure it follows APA style guide and targets an advanced reader. 
    Output in markdown format.
    Text: ```{text}```
    """
    response = get_completion(prompt)
    return response


def gradio_interface(text, mode):
    if mode == "Spell Check (Diff)":
        return spell_check2(text)
    elif mode == "Spell Check (APA Style)":
        return spell_check3(text)
    else:
        return "Select a valid mode."


with gr.Blocks() as demo:
    gr.Markdown("# LLM Review Proofreader")
    text_input = gr.Textbox(label="Enter review text", value=text, lines=10)
    mode = gr.Radio(["Spell Check (Diff)", "Spell Check (APA Style)"], label="Mode", value="Spell Check (Diff)")
    output = gr.Markdown()
    btn = gr.Button("Run")
    btn.click(fn=gradio_interface, inputs=[text_input, mode], outputs=output)


demo.launch()
