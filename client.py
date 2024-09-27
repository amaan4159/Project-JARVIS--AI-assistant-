from openai import OpenAI

client = OpenAI(
    api_key="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"
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
