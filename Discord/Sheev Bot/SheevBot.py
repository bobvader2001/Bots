################################
## Sheev Bot For Discord v1.0 ##
################################

#Written by bobvader2001

import discord
import time
import random
import youtube_dl
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from discord.ext.commands import Bot

token = 'No u'
client = Bot(command_prefix = "!")
botversion = "1.0"

#Startup
@client.event
async def on_ready():
	print("\nTest Bot v" + botversion)
	print("\nClient logged in as:")
	print(client.user.name)
	print(client.user.id)
	print('------------------')
	time.sleep(2)
	await client.change_presence(game=discord.Game(name='The Senate'))

#Function To Play Sound
async def playSound(track, user):
	channel = user.voice.voice_channel
	if(channel is not None):
		try:
			voice = await client.join_voice_channel(channel)
			player = voice.create_ffmpeg_player('C:\\Users\\Matthew\\Documents\\Discord Bots\\Sheev Bot\\SFX\\' + track + '.mp3')
			player.start()
			while True:
				if player.is_done():
					await voice.disconnect()
					print('Played ' + track)
					break
		except:
			await client.say("An error has occured, who knows what it was because I'm too lazy to code in each exception but probably just stop spamming it you skrub")
	else:
		await client.say("You can't play a sound effect unless you are in a voice channel")

####################
## TEXT RESPONSES ##
####################

#Message Content Based Responses
@client.event
async def on_message(message):
	lowered_message = message.content.lower()
	if (lowered_message.startswith('ping')):
		await client.send_message(message.channel, 'Pong!')
	if (lowered_message.startswith('plop')):
		await client.send_message(message.channel, message.author.mention + ' Plop')
	if (lowered_message.startswith('hello') and not lowered_message.startswith("hello there, ")):
		await client.send_message(message.channel, 'Hello there, ' + message.author.mention)
	await client.process_commands(message)

#Version
@client.command()
async def version(*args):
	await client.say("I am Sheev Bot v" + botversion + "\nI am the Senate!")
	print('Displayed Version')

#Tragedy Of Darth Plagueis The Wise
@client.command()
async def tragedy(*args):
	return await client.say("Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It’s not a story the Jedi would tell you. It’s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself.")
	print('Told The Tragedy of Darth Plagueis The Wise')

#RTD
@client.command()
async def rtd(lLimit_input, uLimit_input):
	try:
		lLimit = int(lLimit_input)
		uLimit = int(uLimit_input)
		rolled = random.randint(lLimit, uLimit)
		return await client.say(rolled)
		print('Rolled a dice between ' + lLimit_input + 'and ' + uLimit_input + 'and got ' + str(rolled))
	except:
		return await client.say("You broke it you idiot and I'm not sure why but probably because you tried to use words. Since when does a dice have words on?")

#STFU
@client.command(pass_context=True)
async def stfu(ctx, user):
	await client.say(ctx.message.author.mention + ' says shut the fuck up ' + user)
	print("Told someone to stfu")

#Send Sheev Face
@client.command(pass_context=True)
async def face(ctx):
	return await client.send_file(ctx.message.channel, 'C:\\Users\\Matthew\\Documents\\Discord Bots\\Sheev Bot\\SheevFace.jpg')
	print('Displayed a glorious picture of The Senate')

#Ideal GF
@client.command(pass_context=True)
async def idealgf(ctx):
	try:
		channel = ctx.message.channel
		phrases = []
		path = 'C:\\Users\\Matthew\\Documents\\Discord Bots\\Sheev Bot\\IdealGF.png'
		im = Image.open(path).convert('RGBA')
		size = width, height = im.size
		draw = ImageDraw.Draw(im, 'RGBA')
		font = ImageFont.truetype('arial.ttf', 25)
		titlefont = ImageFont.truetype('arial.ttf', 50)

		async for oldmessage in client.logs_from(channel, limit=1000):
				if oldmessage.author is ctx.message.author and not oldmessage.content.startswith('!') and not '@' in oldmessage.content and len(oldmessage.content) < 25:
						phrases.append(oldmessage)

		selected_phrases = []
		counter = 0
		while(counter < 5):
			random_message_int = random.randint(0, len(phrases)-1)
			random_message_obj = phrases[random_message_int]
			random_message_str = random_message_obj.content
			if(random_message_str not in selected_phrases and random_message_str != ""):
				selected_phrases.append(random_message_str)
				counter += 1
			else:
				continue

		draw.text((200, 100), '"' + selected_phrases[0] + '"', (0, 0, 0, 255), font = font)
		draw.text((30, 200), '"' + selected_phrases[1] + '"', (0, 0, 0, 255), font = font)
		draw.text((400, 400), '"' + selected_phrases[2] + '"', (0, 0, 0, 255), font = font)
		draw.text((50, 450), '"' + selected_phrases[3] + '"', (0, 0, 0, 255), font = font)
		draw.text((150, 525), '"' + selected_phrases[4] + '"', (0, 0, 0, 255), font = font)
		draw.text((100, 10), ctx.message.author.name + ' GF', (0, 0, 0, 255), font = titlefont)
		
		im.save('C:\\Users\\Matthew\\Documents\\Discord Bots\\Sheev Bot\\IdealGFTemp.png', 'PNG')
		return await client.send_file(channel, 'C:\\Users\\Matthew\\Documents\\Discord Bots\\Sheev Bot\\IdealGFTemp.png')
		print("Generated an ideal GF meme")
	except:
		await client.say("Some stupid exception. It's possible there isn't a message that fits the criteria or I'm just bad at maths")

@client.command(pass_context=True)
async def boop(ctx):
	await playSound('Boop', ctx.message.author)

@client.command(pass_context=True)
async def dewit(ctx):
	await playSound('Dew It', ctx.message.author)

@client.command(pass_context=True)
async def happylanding(ctx):
	await playSound('Another Happy Landing', ctx.message.author)

@client.command(pass_context=True)
async def screech(ctx):
	await playSound('Autistic Screeching', ctx.message.author)
	
@client.command(pass_context=True)
async def generalkenobi(ctx):
	await playSound('General Kenobi', ctx.message.author)

@client.command(pass_context=True)
async def healing(ctx):
	await playSound('Healing', ctx.message.author)

@client.command(pass_context=True)
async def hello(ctx):
	await playSound('Hello There', ctx.message.author)

@client.command(pass_context=True)
async def senate(ctx):
	await playSound('I Am The Senate', ctx.message.author)

@client.command(pass_context=True)
async def sand(ctx):
	await playSound('I Don\'t Like Sand', ctx.message.author)

@client.command(pass_context=True)
async def sandF(ctx):
	await playSound('I Don\'t Like Sand Full', ctx.message.author)

@client.command(pass_context=True)
async def highground(ctx):
	await playSound('I Have The High Ground', ctx.message.author)

@client.command(pass_context=True)
async def treason(ctx):
	await playSound('It\'s Treason Then', ctx.message.author)

@client.command(pass_context=True)
async def excuse(ctx):
	await playSound('Jar Jar Exqueese Me', ctx.message.author)

@client.command(pass_context=True)
async def rude(ctx):
	await playSound('Jar Jar How Rude', ctx.message.author)

@client.command(pass_context=True)
async def back(ctx):
	await playSound('Jar Jar Meesa Back', ctx.message.author)

@client.command(pass_context=True)
async def ohno(ctx):
	await playSound('Jar Jar Oh No', ctx.message.author)

@client.command(pass_context=True)
async def smells(ctx):
	await playSound('Jar Jar That Smells', ctx.message.author)

@client.command(pass_context=True)
async def younglings(ctx):
	await playSound('Killing Younglings', ctx.message.author)

@client.command(pass_context=True)
async def liar(ctx):
	await playSound('Liar!', ctx.message.author)

@client.command(pass_context=True)
async def lmg(ctx):
	await playSound('LMG', ctx.message.author)

@client.command(pass_context=True)
async def toomany(ctx):
	await playSound('Master Skywalker With Lightsaber', ctx.message.author)

@client.command(pass_context=True)
async def masterwindu(ctx):
	await playSound('Master Windu', ctx.message.author)

@client.command(pass_context=True)
async def newempire(ctx):
	await playSound('My New Empire', ctx.message.author)

@client.command(pass_context=True)
async def no(ctx):
	await playSound('No', ctx.message.author)

@client.command(pass_context=True)
async def noot(ctx):
	await playSound('Noot Noot', ctx.message.author)

@client.command(pass_context=True)
async def normies(ctx):
	await playSound('Normies', ctx.message.author)

@client.command(pass_context=True)
async def notyet(ctx):
	await playSound('Not Yet', ctx.message.author)

@client.command(pass_context=True)
async def podracing(ctx):
	await playSound('Now This Is Podracing', ctx.message.author)

@client.command(pass_context=True)
async def potato(ctx):
	await playSound('Potato', ctx.message.author)

@client.command(pass_context=True)
async def shreck(ctx):
	await playSound('Shreck Hello', ctx.message.author)

@client.command(pass_context=True)
async def surprise(ctx):
	await playSound('Surprise', ctx.message.author)

@client.command(pass_context=True)
async def takeaseat(ctx):
	await playSound('Take A Seat', ctx.message.author)

@client.command(pass_context=True)
async def trust(ctx):
	await playSound('Trust', ctx.message.author)

@client.command(pass_context=True)
async def power(ctx):
	await playSound('Unlimited Power', ctx.message.author)

@client.command(pass_context=True)
async def yee(ctx):
	await playSound('Yee', ctx.message.author)

@client.command(pass_context=True)
async def yipee(ctx):
	await playSound('Yipee', ctx.message.author)

@client.command(pass_context=True)
async def arrest(ctx):
	await playSound('You Are Under Arrest Chancellor', ctx.message.author)

@client.command(pass_context=True)
async def lost(ctx):
	await playSound('You Have Lost', ctx.message.author)

@client.command(pass_context=True)
async def fast(ctx):
	select = random.randint(1,5)
	await playSound('Fast ' + str(select), ctx.message.author)

@client.command(pass_context=True)
async def fastF(ctx):
	select = random.randint(1,3)
	await playSound('Fast Full ' + str(select), ctx.message.author)

@client.command(pass_context=True)
async def nope(ctx):
	await playSound('Nope', ctx.message.author)

@client.command(pass_context=True)
async def hithere(ctx):
	await playSound('Hi There', ctx.message.author)

@client.command(pass_context=True)
async def vsauce(ctx):
	await playSound('Vsauce Michael', ctx.message.author)

@client.command(pass_context=True)
async def retard(ctx):
	await playSound('Retard Alert', ctx.message.author)

@client.command(pass_context=True)
async def bighole(ctx):
	await playSound('Big Hole', ctx.message.author)

@client.command(pass_context=True)
async def getout(ctx):
	await playSound('Normies Get Out', ctx.message.author)

@client.command(pass_context=True)
async def yeehaw(ctx):
	await playSound('Yee Haw', ctx.message.author)

@client.command(pass_context=True)
async def cyka(ctx):
	await playSound('Cyka Blyat', ctx.message.author)


#Questionable Sounds
'''
@client.command(pass_context=True)
async def johncena(ctx):
	await playSound('John Cena', ctx.message.author)

@client.command(pass_context=True)
async def bloodsugar(ctx):
	await playSound('Blood Sugar Spam', ctx.message.author)

@client.command(pass_context=True)
async def weeb(ctx):
	await playSound('CaramelDansen Ryu Remix', ctx.message.author)

@client.command(pass_context=True)
async def somebody(ctx):
	await playSound('Somebody Once Told Me', ctx.message.author)
'''

client.run(token)