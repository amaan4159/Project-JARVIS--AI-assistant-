from openai import OpenAI

client = OpenAI(
    api_key="API KEY of open ai"
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like alexa and google cloud"},
        {
            "role": "user",
            "content": "What is life?"
        }
    ]
)

print(completion.choices[0].message.content)
