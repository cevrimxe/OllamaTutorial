import ollama

# Initialize the Ollama client
client = ollama.Client()

# Define the model
model = "llama3.2"  # Model ismini kendine göre değiştir

# Define the base prompt (system message)
base_prompt = ""


# Define the user prompt
user_prompt = "What is Python?"

# Send the query to the model with a base prompt
response = client.chat(
    model=model,
    messages=[
        {"role": "system", "content": base_prompt},  # Base prompt burada tanımlanıyor
        {"role": "user", "content": user_prompt}
    ]
)

# Print the response from the model
print("Response from Ollama:")
print(response["message"]["content"])
