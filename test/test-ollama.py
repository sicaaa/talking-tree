
# A simple code to test ollama and the gemma3 model


import ollama

response = ollama.chat(
    model='gemma3',
    messages=[
        {'role': 'user', 'content': 'Explain the effects of UV radiation on birch trees in one sentence.'}
    ]
)

print(response['message']['content'])


