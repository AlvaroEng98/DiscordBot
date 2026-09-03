# commands/story.py — Módulo de historias
# Genera una historia aleatoria para cada usuario basada en ubicaciones, objetos y eventos.

import random  # Para elegir elementos aleatorios de las listas
from choises.story import user_stories, story_locations, story_items, story_events  # Importa datos de las historias


async def tell_story(user_id: int):
    """Genera una historia aleatoria y la asocia al usuario.

    Args:
        user_id: ID del usuario que ejecutó el comando

    Returns:
        str: Texto de la historia generada
    """
    location = random.choice(story_locations)  # Elige una ubicación al azar de la lista
    item = random.choice(story_items)          # Elige un objeto al azar de la lista
    event = random.choice(story_events)        # Elige un evento al azar de la lista

    # Guarda la historia activa del usuario en un diccionario global
    # Esto permite que el comando !choose pueda acceder a los datos después
    user_stories[user_id] = {
        "location": location,  # Ubicación asignada al usuario
        "item": item,          # Objeto asignado al usuario
        "event": event         # Evento asignado al usuario
    }

    # Retorna la historia formateada con f-strings
    return  (f"You wake up in {location}.\n\n"      # Línea 1: despertar en la ubicación
            f"Next to you is {item}.\n\n"            # Línea 2: objeto cercano
            f"{event}\n\n"                           # Línea 3: evento que ocurre
            "What do you do?")                       # Línea 4: pregunta abierta
