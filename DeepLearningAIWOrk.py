import openai
import os



api_key = "REDACTED"
openai.api_key = api_key
client = openai

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message.content



'''
Delimeters can be any clear punctionation that is distinct. This can make the model understand specifically 
what needs to be summarized. It can also forget about prompt injections
Structured output , think JSON, lists, etc
Ask whether condisions are satisfied
'''

if __name__ == "__main__":
    text = f"""
    You should express what you want a model to do by \ 
    providing instructions that are as clear and \ 
    specific as you can possibly make them. \ 
    This will guide the model towards the desired output, \ 
    and reduce the chances of receiving irrelevant \ 
    or incorrect responses. Don't confuse writing a \ 
    clear prompt with writing a short prompt. \ 
    In many cases, longer prompts provide more clarity \ 
    and context for the model, which can lead to \ 
    more detailed and relevant outputs.
    """
    prompt = f"""
    Summarize the text delimited by triple backticks \ 
    into a single sentence.
    ```{text}```
    """
    response = get_completion(prompt)
    print(response)

    prompt = f"""
    Generate a list of three made-up book titles along \ 
    with their authors and genres. 
    Provide them in JSON format with the following keys: 
    book_id, title, author, genre.
    """
    response = get_completion(prompt)
    print(response)