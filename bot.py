# ============================================================
# bot.py — Archivo principal del bot de Discord
# ============================================================

# Importar librerías del sistema y de terceros
import os              # Para acceder a variables de entorno del sistema operativo
import threading       # Para ejecutar el servidor HTTP en un hilo separado
from http.server import HTTPServer, BaseHTTPRequestHandler  # Servidor HTTP ligero para health checks
import discord         # Librería principal para interactuar con la API de Discord
from discord.ext import commands  # Framework de comandos de discord.py
from dotenv import load_dotenv     # Para cargar variables de entorno desde un archivo .env
from choises.help import help_response
# Importar módulos de comandos del bot
from commands.hello import send_hello      # Función que saluda al usuario
from commands.choose import select_choose  # Función que procesa elecciones del usuario
from commands.story import tell_story, user_stories  # Función de historias y diccionario de historias activas
from commands.chat import select_chat      # Función que genera respuestas de chat

# ------------------------------------------------------------
# Configuración de variables de entorno
# ------------------------------------------------------------
load_dotenv()  # Carga las variables del archivo .env al entorno del sistema

TOKEN = os.getenv("DISCORD_TOKEN")  # Obtiene el token del bot de Discord desde las variables de entorno


# ============================================================
# Servidor de salud (Health Check)
# Usado para mantener el bot activo en plataformas de hosting
# como Render o Railway, que verifican que el servicio responda.
# ============================================================
class HealthHandler(BaseHTTPRequestHandler):
    """Manejador HTTP que responde 'OK' a cualquier petición GET o HEAD."""

    def do_GET(self):
        """Responde con estado 200 y cuerpo 'OK' cuando recibimos un GET."""
        self.send_response(200)       # Envía el código de estado HTTP 200 (éxito)
        self.end_headers()            # Finaliza los encabezados de la respuesta
        self.wfile.write(b"OK")       # Escribe "OK" como cuerpo de la respuesta (bytes)

    def do_HEAD(self):
        """Responde con estado 200 sin cuerpo, para verificaciones de salud."""
        self.send_response(200)       # Envía código de estado 200
        self.end_headers()            # Finaliza encabezados (sin contenido en el cuerpo)

    def log_message(self, format, *args):
        """Sobrescribe el log para silenciar las peticiones HTTP en consola."""
        pass  # No imprime nada, evita ruido en la terminal


def start_health_server():
    """Inicia un servidor HTTP en un puerto configurable (default: 8080)."""
    port = int(os.getenv("PORT", 8080))                         # Obtiene el puerto de la variable PORT o usa 8080
    server = HTTPServer(("0.0.0.0", port), HealthHandler)       # Crea el servidor escuchando en todas las interfaces (0.0.0.0)
    server.serve_forever()                                       # Ejecuta el servidor indefinidamente


# ============================================================
# Configuración del bot de Discord
# ============================================================
intents = discord.Intents.default()   # Crea un conjunto de intents (permisos) por defecto de Discord
intents.message_content = True        # Habilita la lectura del contenido de los mensajes (necesario para !comandos)

bot = commands.Bot(
    command_prefix="!",               # Define "!" como el prefijo para activar comandos (ej: !hello)
    intents=intents                   # Asigna los intents configurados al bot
)


# ============================================================
# Eventos del bot
# ============================================================
@bot.event                            # Decorador que registra una función como evento de Discord
async def on_ready():
    """Se ejecuta una vez que el bot se conecta exitosamente a Discord."""
    print(f"Logged in as {bot.user}")  # Imprime en consola el nombre del bot conectado


# ============================================================
# Comandos del bot
# ============================================================
@bot.command()                        # Registra la función como un comando invocable con !hello
async def hello(ctx):
    """Comando !hello — Saluda al usuario con un mensaje fijo."""
    await ctx.send(await send_hello())  # Ejecuta send_hello() y envía el resultado al canal de Discord


@bot.command()                        # Registra el comando !story
async def story(ctx):
    """Comando !story — Genera una historia aleatoria para el usuario."""
    user_id = ctx.author.id           # Obtiene el ID único del usuario que ejecutó el comando

    story_text = await tell_story(user_id)  # Genera una historia aleatoria y la guarda en user_stories
    await ctx.send(story_text)        # Envía el texto de la historia al canal de Discord


@bot.command()                        # Registra el comando !choose
async def choose(ctx, choice: str):
    """Comando !choose <left|right> — Permite al usuario elegir un camino en su historia."""
    user_id = ctx.author.id           # Obtiene el ID del usuario que ejecutó el comando

    if user_id not in user_stories:   # Verifica si el usuario tiene una historia activa
        await ctx.send("You don't have an active story. Try `!story` first.")  # Mensaje si no tiene historia
        return                        # Sale de la función sin hacer nada más

    choice_text = await select_choose(user_id, choice)  # Procesa la elección y genera la respuesta
    await ctx.send(choice_text)       # Envía el resultado al canal de Discord


@bot.command()                        # Registra el comando !chat
async def chat(ctx, *, message: str):
    """Comando !chat <mensaje> — Responde basado en palabras clave del mensaje."""
    response = await select_chat(message)  # Busca coincidencia por palabra clave y retorna respuesta
    await ctx.send(response)              # Envía la respuesta al canal de Discord

@bot.command()
async def support(ctx, *, message: str):

    response = await support_responses(message)
    await ctx.send(response)

@bot.command()
async def help(ctx):

    await ctx.send(help_response)


#En caso de introducir un comando erroneo se lanza este error
@bot.event
async def on_command(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(
            "You're missing something. Try `!help` to see how the command works."
        )

    elif isinstance(error, commands.CommandNotFound):
        return

    else:
        print(f"Error: {error}")



# ============================================================
# Inicio del bot
# ============================================================
# Lanza el servidor de salud en un hilo separado (daemon=True = se cierra con el programa principal)
threading.Thread(target=start_health_server, daemon=True).start()

# Conecta el bot a Discord usando el token (esto bloquea y ejecuta el bot indefinidamente)
bot.run(TOKEN)
