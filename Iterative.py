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


fact_sheet_chair = """
OVERVIEW
- Part of a beautiful family of mid-century inspired office furniture, 
including filing cabinets, desks, bookcases, meeting tables, and more.
- Several options of shell color and base finishes.
- Available with plastic back and front upholstery (SWC-100) 
or full upholstery (SWC-110) in 10 fabric and 6 leather options.
- Base finish options are: stainless steel, matte black, 
gloss white, or chrome.
- Chair is available with or without armrests.
- Suitable for home or business settings.
- Qualified for contract use.

CONSTRUCTION
- 5-wheel plastic coated aluminum base.
- Pneumatic chair adjust for easy raise/lower action.

DIMENSIONS
- WIDTH 53 CM | 20.87”
- DEPTH 51 CM | 20.08”
- HEIGHT 80 CM | 31.50”
- SEAT HEIGHT 44 CM | 17.32”
- SEAT DEPTH 41 CM | 16.14”

OPTIONS
- Soft or hard-floor caster options.
- Two choices of seat foam densities: 
medium (1.8 lb/ft3) or high (2.8 lb/ft3)
- Armless or 8 position PU armrests 

MATERIALS
SHELL BASE GLIDER
- Cast Aluminum with modified nylon PA6/PA66 coating.
- Shell thickness: 10 mm.
SEAT
- HD36 foam

COUNTRY OF ORIGIN
- Italy
"""


def issue_1():
    prompt_1 = f"""
    Your task is to help a marketing team create a 
    description for a retail website of a product based 
    on a technical fact sheet.

    Write a product description based on the information 
    provided in the technical specifications delimited by 
    triple backticks.

    Technical specifications: ```{fact_sheet_chair}```
    """
    prompt_2 = f"""
    Your task is to help a marketing team create a 
    description for a retail website of a product based 
    on a technical fact sheet.

    Write a product description based on the information 
    provided in the technical specifications delimited by 
    triple backticks.

    Use at most 50 words.

    Technical specifications: ```{fact_sheet_chair}```
    """
    response_1 = get_completion(prompt_1)
    print("Completion for prompt 1:")
    print(response_1)

    response_2 = get_completion(prompt_2)
    print("Completion for prompt 2:")
    print(response_2)


def issue_2():
    prompt_1 = f"""
    Your task is to help a marketing team create a 
    description for a retail website of a product based 
    on a technical fact sheet.

    Write a product description based on the information 
    provided in the technical specifications delimited by 
    triple backticks.

    The description is intended for furniture retailers, 
    so should be technical in nature and focus on the 
    materials the product is constructed from.

    Use at most 50 words.

    Technical specifications: ```{fact_sheet_chair}```
    """
    prompt_2 = f"""
    Your task is to help a marketing team create a 
    description for a retail website of a product based 
    on a technical fact sheet.

    Write a product description based on the information 
    provided in the technical specifications delimited by 
    triple backticks.

    The description is intended for furniture retailers, 
    so should be technical in nature and focus on the 
    materials the product is constructed from.

    At the end of the description, include every 7-character 
    Product ID in the technical specification.

    Use at most 50 words.

    Technical specifications: ```{fact_sheet_chair}```
    """
    response_1 = get_completion(prompt_1)
    print("Completion for prompt 1:")
    print(response_1)

    response_2 = get_completion(prompt_2)
    print("Completion for prompt 2:")
    print(response_2)


def issue_3():
    prompt = f"""
    Your task is to help a marketing team create a 
    description for a retail website of a product based 
    on a technical fact sheet.

    Write a product description based on the information 
    provided in the technical specifications delimited by 
    triple backticks.

    The description is intended for furniture retailers, 
    so should be technical in nature and focus on the 
    materials the product is constructed from.

    At the end of the description, include every 7-character 
    Product ID in the technical specification.

    After the description, include a table that gives the 
    product's dimensions. The table should have two columns.
    In the first column include the name of the dimension. 
    In the second column include the measurements in inches only.

    Give the table the title 'Product Dimensions'.

    Format everything as HTML that can be used in a website. 
    Place the description in a <div> element.

    Technical specifications: ```{fact_sheet_chair}```
    """

    response = get_completion(prompt)
    print(response)


def main():
    #issue_1()
    #issue_2()
    issue_3()


if __name__ == "__main__":
    main()