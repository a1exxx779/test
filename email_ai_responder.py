import openai
import os

# Set your OpenAI API key (replace with your actual key)
openai.api_key = "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"

def chat_with_openai(prompt):
    """Generates a response using OpenAI GPT model"""
    response = openai.ChatCompletion.create(
        model="gpt-4",  # You can use "gpt-3.5-turbo" or other available models
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    print("🤖 OpenAI Chatbot (type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye! 👋")
            break
        response = chat_with_openai(user_input)
        print("AI:", response)