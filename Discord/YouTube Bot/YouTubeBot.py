import discord
import time
import random
import youtube_dl
from discord.ext.commands import Bot

token = 'No u'
client = Bot(command_prefix = "~")
botversion = "0.1"

#Startup
@client.event
async def on_ready():
	print("\YouTube Bot v" + botversion)
	print("\nClient logged in as:")
	print(client.user.name)
	print(client.user.id)
	print('------------------')
	time.sleep(2)
	await client.change_presence(game=discord.Game(name='YouTube'))

async def playVid(link):
	try:
		channel = client.get_channel('210735188798341122')
		voice = await client.join_voice_channel(channel)
		ytplayer = await voice.create_ytdl_player(link)
		ytplayer.start()
		while True:
			if ytplayer.is_done():
				await voice.disconnect()
				break
	except:
		await client.say("An error has occured, who knows what it was because I'm too lazy to code in each exception but probably just stop spamming it you skrub")

@client.command()
async def play(link):
	await playVid(link)

@client.command()
async def stop(*args):
	await voice.disconnect()


client.run(token)