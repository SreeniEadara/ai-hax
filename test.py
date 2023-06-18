import openai

OPENAI_API_KEY = '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'
openai.api_key = OPENAI_API_KEY

messages = [
    {"role": "user", "content": "As an intelligent AI model, if you could be any fictional character, who would you choose and why?"}
]

response = openai.ChatCompletion.create(
    model="gpt-4",
    max_tokens=100,
    temperature=1.2,
    messages=messages
)

print(response)