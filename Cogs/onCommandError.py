import discord
from discord.ext import commands
from discord.ext.commands import MissingPermissions, CheckFailure, CommandNotFound
import time

# Una clase que define que hacer si el usuario no tiene permiso de correr un comando,
#  o si es que superó el límite de veces que se puede llamar
class OnCommandErrorCog(commands.Cog, name="on command error"):
	def __init__(self, bot:commands.Bot):
		self.bot = bot
        
	@commands.Cog.listener()
	async def on_command_error(self, ctx:commands.Context, error:commands.CommandError):
		if isinstance(error, commands.CommandOnCooldown):
			day = round(error.retry_after/86400)
			hour = round(error.retry_after/3600)
			minute = round(error.retry_after/60)
			if day > 0:
				await ctx.send('Espera! Podrás correr este comando nuevamente en '+str(day)+ "día(s)", delete_after=15)
			elif hour > 0:
				await ctx.send('Espera! Podrás correr este comando nuevamente en '+str(hour)+ " hora(s)", delete_after=15)
			elif minute > 0:
				await ctx.send('Espera! Podrás correr este comando nuevamente en '+ str(minute)+" minuto(s)", delete_after=15)
			else:
				await ctx.send(f'Espera! Podrás correr este comando nuevamente en {error.retry_after:.2f} segundo(s)', delete_after=15)
		elif isinstance(error, CommandNotFound):
			return
		elif isinstance(error, MissingPermissions):
 			await ctx.send(error.text)
		elif isinstance(error, CheckFailure):
			await ctx.send(error.original.text)
		else:
			print(error) 

def setup(bot):
	bot.add_cog(OnCommandErrorCog(bot))