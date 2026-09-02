import os
import random
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
import discord
from discord.ext import commands
from dotenv import load_dotenv
from commands.hello import send_hello
from commands.choose import select_choose
from commands.story import tell_story, user_stories

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

    def do_HEAD(self):
        self.send_response(200)
        self.end_headers()

    def log_message(self, format, *args):
        pass


def start_health_server():
    port = int(os.getenv("PORT", 8080))
    server = HTTPServer(("0.0.0.0", port), HealthHandler)
    server.serve_forever()


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def hello(ctx):
    await ctx.send(send_hello)

@bot.command()
async def story(ctx):
    user_id = ctx.author.id

    story_text = await tell_story(user_id)
    await ctx.send(story_text)

@bot.command()
async def choose(ctx, choice: str):
    user_id = ctx.author.id

    if user_id not in user_stories:
        await ctx.send("You don't have an active story. Try `!story` first.")
        return



    choice_text = await select_choose(user_id, choice)
    await ctx.send(choice_text)

chat_responses = {
    "hello": [
        "Hey! What's up?",
        "Hello! How's your day going?",
        "Hi! What are you working on?"
    ],
    "python": [
        "Python is a great language for beginners because its syntax is pretty readable.",
        "If you're learning Python, try building something instead of only watching tutorials."
    ],
    "discord": [
        "Discord bots are a fun way to practice Python because you get instant feedback.",
        "Once you understand commands and events, you can build some surprisingly complex bots."
    ]
}

@bot.command()
async def chat(ctx, *, message: str):
    text = message.lower()

    for keyword, responses in chat_responses.items():
        if keyword in text:
            await ctx.send(random.choice(responses))
            return

    await ctx.send(
        "I'm still learning how to respond to that. "
        "Try talking to me about Python or Discord!"
    )


threading.Thread(target=start_health_server, daemon=True).start()
bot.run(TOKEN)