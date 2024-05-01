from openai import OpenAI

from config import api_key

# Inicializar el cliente de OpenAI con la API key
client = OpenAI(api_key=api_key)

def chat_with_gpt(prompt, chat_history):
    # Añadir la última entrada del usuario al historial de chat
    chat_history.append({"role": "user", "content": prompt})
    
    # Generar la completación del chat usando el historial actualizado
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=chat_history
    )
    
    # Extraer el texto de la respuesta
    response_text = response.choices[0].message.content.strip()
    
    # Añadir la respuesta del sistema al historial de chat
    chat_history.append({"role": "system", "content": response_text})

    return response_text, chat_history

if __name__ == "__main__":
    chat_history = []  # Inicializar el historial de chat
    print("ChatGPT Sesión Iniciada. Escribe 'quit', 'exit' o 'bye' para salir.")
    while True:
        user_input = input("Tú: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("ChatGPT Sesión Terminada.")
            break
        response, chat_history = chat_with_gpt(user_input, chat_history)
        print("ChatGPT:", response)