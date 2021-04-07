import discord
from discord.ext import commands
import json

# Lée el token y el prefijo del bot a usar
with open("configuration.json", "r") as config:
    data = json.load(config)
    token = data["token"]
    prefix = data["prefix"]

# Intents. Una configuración algo nueva de discord:
# https://discordpy.readthedocs.io/en/latest/intents.html
# TL;DR: Si queremos leer estados de usuario, necesitamos activar "presences"
#        Si queremos detectar cambios de usuarios como cambios de nombre, foto,
#		   o si un usuario entró o salió del erver, necesitamos activar "members"
intents = discord.Intents.default() # Esto activa todo menos los 2 de arriba
bot = commands.Bot(prefix, intents = intents)

# Los cogs que queremos que el bot use. Son los nombres de los archivos en la carpeta Cogs
initial_extensions = [
 "Cogs.onCommandError",
 "Cogs.help",
 "Cogs.ping",
 "Cogs.tools",
 "Cogs.cleanCommands"
]

print(initial_extensions)

if __name__ == '__main__':
    # Añade los cogs al bot
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f"No pudimos ingresar la extensión {extension}")

# Aquí cambiamos el estado del bot
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name =f"{bot.command_prefix}help"))
    print(discord.__version__)


bot.run(token)