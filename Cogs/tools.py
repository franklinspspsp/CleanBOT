import discord
from discord.ext import commands
import romkan

# En esta clase definimos los comandos de este cog
class Tools(commands.Cog, name="BotTools"):

    # Cosas que hacer la primera vez que cargamos este Cog en el bot
    def __init__(self, bot:commands.Bot):
        self.bot = bot

    # Comando
    @commands.command(name = "reload",
                    usage="<usage>",
                    description = "Actualiza los cogs del bot")
    @commands.guild_only()
    @commands.cooldown(1, 10, commands.BucketType.member)
    async def reloadCogs(self, ctx:commands.Context):
        cogs  = [
            "Cogs.onCommandError", "Cogs.help", "Cogs.ping", "Cogs.tools",
            "Cogs.cleanCommands"
        ]
        for cog_name in cogs:
            self.bot.reload_extension(cog_name)

        await ctx.send("Reload complete ✅")#,delete_after=15)


    @commands.command(name = "romanjinice",
                    aliases=["roma","rmj"],
                    usage="romanjinice <texto en Kana>",
                    description = "Convierte Kana a Romanji")
    async def reloadCogs(self, ctx:commands.Context):
        # Transform to romanji
        romanjinized = romkan.to_roma(ctx.message.content)
        # Remove command from result (This removes the first word)
        # TODO: If user sends the command and the text in different lines,
        #       this code will remove everythong until it finds a space (deleting a lo of text)
        #       Solution: Detect this and crop until a \n 
        romanjinized = romanjinized[romanjinized.find(" ")+1:]
        # Send result
        await ctx.send(romanjinized)

def setup(bot:commands.Bot):
    bot.add_cog(Tools(bot))