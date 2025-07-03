from openai import OpenAI

client = OpenAI(
    api_key="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",
)

completion = client.chat.completions.create(
    model="gpt-4.1",
    messages=[
        {
            "role": "user",
            "content": "Write a one-sentence bedtime story about a unicorn."
        }
    ]
)

print(completion.choices[0].message.content)