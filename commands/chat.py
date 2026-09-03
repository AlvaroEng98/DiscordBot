# commands/chat.py — Módulo de chat
# Responde al usuario basándose en palabras clave de su mensaje.

import random  # Para elegir una respuesta al azar de la lista
from choises.chats import chat_responses  # Importa el diccionario de respuestas desde choises


async def select_chat(message: str):
    """Procesa el mensaje del usuario y retorna una respuesta basada en palabras clave.

    Args:
        message: Texto que escribió el usuario en el comando !chat

    Returns:
        str: Respuesta generada (coincidencia o mensaje por defecto)
    """
    text = message.lower()  # Convierte a minúsculas para comparar sin importar mayúsculas

    for keyword, responses in chat_responses.items():  # Recorre cada palabra clave y su lista de respuestas
        if keyword in text:           # Si la palabra clave está dentro del mensaje del usuario
            return random.choice(responses)  # Elige una respuesta al azar y la retorna

    # Si no se encontró ninguna palabra clave, retorna respuesta por defecto
    return (
        "I'm still learning how to respond to that. "
        "Try talking to me about Python or Discord!"
    )
