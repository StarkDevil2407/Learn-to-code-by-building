import openai
import os

def ask_openai(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        print("❌ Set your API key as environment variable 'OPENAI_API_KEY'")
        return

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=100
    )
    print("Response:", response.choices[0].text.strip())

if __name__ == "__main__":
    question = input("Ask something: ")
    ask_openai(question)
