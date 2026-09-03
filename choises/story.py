# choises/story.py — Datos de las historias
# Contiene las listas de ubicaciones, objetos y eventos, y el diccionario de historias activas.

# Diccionario que almacena la historia activa de cada usuario
# Clave: user_id (int) | Valor: dict con keys "location", "item", "event"
user_stories = {}

# Lista de posibles ubicaciones para las historias
story_locations = [
    "an abandoned library",       # Una biblioteca abandonada
    "a mysterious island",        # Una isla misteriosa
    "a futuristic city",          # Una ciudad futurista
    "a hidden underground laboratory",  # Un laboratorio subterráneo oculto
    "a forest that never appears on maps"  # Un bosque que no aparece en mapas
]

# Lista de posibles objetos que el usuario puede encontrar
story_items = [
    "a glowing key",              # Una llave brillante
    "an ancient notebook",        # Un cuaderno antiguo
    "a strange compass",          # Una brújula extraña
    "a locked metal box",         # Una caja metálica cerrada
    "a mysterious photograph"     # Una fotografía misteriosa
]

# Lista de posibles eventos que pueden ocurrir
story_events = [
    "You hear footsteps behind you.",              # Se escuchan pasos detrás
    "The lights suddenly turn off.",               # Las luces se apagan repentinamente
    "A hidden door opens nearby.",                 # Se abre una puerta oculta
    "Your phone starts displaying a message from an unknown sender.",  # Aparece un mensaje anónimo
    "You notice that the room has changed."        # La habitación ha cambiado
]
