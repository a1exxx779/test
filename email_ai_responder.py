import openai
import os


openai.api_key = ""

def chat_with_openai(prompt):
    """Generates a response using OpenAI GPT model"""
    response = openai.ChatCompletion.create(
        model="gpt-4",  
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
