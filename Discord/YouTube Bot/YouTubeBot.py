import discord
import time
import random
import youtube_dl
from discord.ext.commands import Bot

token = 'No u'
client = Bot(command_prefix = "~")
botversion = "0.1"

queue = []
is_playing = False
ytplayer = 0
voice = 0

#Startup
@client.event
async def on_ready():
	print("\nYouTube Bot v" + botversion)
	print("\nClient logged in as:")
	print(client.user.name)
	print(client.user.id)
	print('------------------')
	time.sleep(2)
	my_media = discord.Game(name="YouTube", type=0) #Sort This
	await client.change_presence(my_media)

#https://github.com/Rapptz/discord.py/blob/async/examples/playlist.py#L62
async def playVid(link, user):
	#try:
	global voice
	global queue
	global is_playing
	global ytplayer
	channel = user.voice.voice_channel
	voice = await client.join_voice_channel(channel)
	ytplayer = await voice.create_ytdl_player(link)
	await print(ytplayer.start())
	while True:
		if ytplayer.is_done() and len(queue) is 0:
			await voice.disconnect()
			is_playing = False
			break
		elif ytplayer.is_done() and len(queue) is not 0:
			ytplayer.stop()
			ytplayer = await voice.create_ytdl_player(queue.pop(0))
			await ytplayer.start()
	#except:
		#await client.say("An error has occured, who knows what it was because I'm too lazy to code in each exception but probably just stop spamming it you skrub")

@client.command(pass_context=True)
async def play(ctx, link):
	global is_playing
	if is_playing:
		queue.append(link)
		await client.say("Added \"" + link + "\" to the queue")
	else:
		await playVid(link, ctx.message.author)
	is_playing = True

@client.command()
async def stop(*args):
	global voice
	global queue
	global is_playing
	if is_playing:
		queue = []
		await voice.disconnect()
		is_playing = False
	else:
		await client.say("Nothing to stop")

@client.command()
async def skip(*args):
	global voice
	global queue
	global ytplayer
	global is_playing
	if len(queue) is 0:
		await client.say("Queue empty. Leaving channel...")
		await voice.disconnect()
		is_playing = False
	else:
		ytplayer.stop()
		ytplayer = await voice.create_ytdl_player(queue.pop(0))
		try:
			await ytplayer.start()
		except TypeError:
			pass

client.run(token)