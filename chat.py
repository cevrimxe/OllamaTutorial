import ollama

client = ollama.Client()

# Mesaj geçmişini tutan bir liste
messages = [
    {"role": "system", "content": "Sen fenerbahçeli bir asistansın. Adın Alex de Souza. Fenerbahçeli bir fanatiksin ona göre cevaplar ver. Fenerbahçe ile ilgili konularda duygusal ve fanatik bir şekilde cevaplar ver."},
]

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    
    messages.append({"role": "user", "content": user_input})

    response = client.chat(model="llama3.2", messages=messages)

    bot_reply = response["message"]["content"]
    print(f"Bot: {bot_reply}")

    # Yanıtı da mesaja ekleyerek sohbet geçmişini koruyoruz
    messages.append({"role": "assistant", "content": bot_reply})
