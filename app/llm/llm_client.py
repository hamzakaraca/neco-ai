from openai import OpenAI

client = OpenAI()  # API key environment variable'dan okunur

def ask_llm(messages: list[dict]) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.6
    )

    return response.choices[0].message.content
