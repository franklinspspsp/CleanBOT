import discord
from discord.ext import commands


class cleanCommands(commands.Cog):
    def __init__(self, bot:commands.Bot):
        self.bot = bot


    @commands.command(name = "commandName",
                    usage="<usage>",
                    description = "description")
    @commands.guild_only()
    @commands.cooldown(1, 2, commands.BucketType.member)
    async def commandName(self, ctx:commands.Context):
        await ctx.send("template command")


def setup(bot:commands.Bot):
    bot.add_cog(cleanCommands(bot))