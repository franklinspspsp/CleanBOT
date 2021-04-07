import discord
from discord.ext import commands

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


def setup(bot:commands.Bot):
    bot.add_cog(Tools(bot))