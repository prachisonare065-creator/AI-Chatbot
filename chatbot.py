# ✅ Python project setup
# ✅ Virtual environment
# ✅ Ollama install
# ✅ llama3.2 AI model
# ✅ requests install
# ✅ Python → Ollama connection
# ✅ AI ka real response 🤖
import requests

print("🤖 AI Chatbot")
print("Type 'bye' to exit")

while True:

    user = input("You: ")

    if user.lower() == "bye":
        print("Bot: Goodbye! 👋")
        break

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3.2",
            "prompt": user,
            "stream": False
        }
    )

    data = response.json()

    print("Bot:", data["response"])