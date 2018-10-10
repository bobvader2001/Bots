import discord
import time
import random
import youtube_dl
from discord.ext.commands import Bot

token = 'No u'
client = Bot(command_prefix = "~")
botversion = "0.1"

roles = {"black":"364117952280395776", "blue":"364118187522129931", "yellow":"364118339649404938", "purple":"495628690751750144"}

#Startup
@client.event
async def on_ready():
	print("\nRole Bot v" + botversion)
	print("\nClient logged in as:")
	print(client.user.name)
	print(client.user.id)
	print('------------------')

#Role Function
async def role(message, role):
	for i in roles:
		if(discord.utils.get(message.server.roles, id=roles[i]) in message.author.roles):
			await client.say("You already have a team role!")
			return

	role_obj = discord.utils.get(message.server.roles, id=roles[role])
	await client.add_roles(message.author, role_obj)
	await client.say("Added " + message.author.mention + " to " + role.title() + " Team!")

#Role Commands
@client.command(pass_context=True)
async def black(ctx, *args):
	await role(ctx.message, "black")

@client.command(pass_context=True)
async def blue(ctx, *args):
	await role(ctx.message, "blue")

@client.command(pass_context=True)
async def yellow(ctx, *args):
	await role(ctx.message, "yellow")

@client.command(pass_context=True)
async def purple(ctx, *args):
	await role(ctx.message, "purple")


client.run(token)