# commands/choose.py — Módulo de elecciones
# Permite al usuario elegir entre caminos "left" o "right" en la historia.

async def select_choose(user_id: int, choice: str):
    """Procesa la elección del usuario y genera una respuesta narrativa.

    Args:
        user_id: ID del usuario que hace la elección
        choice: Texto que escribió el usuario (ej: "left", "right")

    Returns:
        str: Texto descriptivo del resultado de su elección
    """
    choice = choice.lower()  # Convierte la elección a minúsculas para comparar sin importar mayúsculas

    if choice == "left":     # Si el usuario eligió "izquierda"
        response = (
            "You head left and discover a room filled with old maps. "  # Descripción del camino izquierdo
            "One of them has your name written on it."                  # Detalle narrativo sorpresa
        )

    elif choice == "right":  # Si el usuario eligió "derecha"
        response = (
            "You head right and find a staircase leading toward "  # Descripción del camino derecho
            "a strange blue light."                                # Elemento misterioso
        )

    else:                   # Si la elección no es válida (ni "left" ni "right")
        response = "Try choosing `left` or `right`."  # Mensaje de error pidiendo una opción válida

    return response  # Retorna la respuesta generada
