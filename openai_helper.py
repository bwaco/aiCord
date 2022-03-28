import os, openai, json

openai.api_key = json.load(open('config.json'))['openai_api_key']

def ask_openai(question):
    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=f'Answer this question with detail:\n\nQuestion: {question}',
        temperature=0.55,
        max_tokens=3400,
        top_p=1,
        best_of=3,
        frequency_penalty=0.425,
        presence_penalty=0.275
    )
    print(response)
    return response['choices'][0]['text']