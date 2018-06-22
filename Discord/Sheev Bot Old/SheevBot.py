################################
## Sheev Bot For Discord v0.4 ##
################################

#Written by bobvader2001

import discord
import time
import random
import youtube_dl
from discord.ext.commands import Bot

token = 'No u'
sheev = Bot(command_prefix = "!")
botversion = "0.4"
angeryState = False
heaseState = False
bannedUsers = []

#Startup
@sheev.event
async def on_ready():
	print("\nSheev Bot v" + botversion)
	print("\nClient logged in as:")
	print(sheev.user.name)
	print(sheev.user.id)
	print('------------------')
	time.sleep(2)
	await sheev.change_presence(game=discord.Game(name='The Senate'))

#Ban Commanmd
@sheev.command()
async def ban(userId):
	global bannedUsers
	userObj = sheev.get_user_info(userId)
	bannedUsers.append(userObj)
	await sheev.say('Banned ' + str(userObj) + ' from the dank memes')
	print(bannedUsers)

@sheev.command(pass_context=True)
async def test(ctx):
	await sheev.say(str(ctx.message.author))

#Angery Mode Toggle
@sheev.command()
async def angery():
	global angeryState
	angeryState = not angeryState
	await sheev.say('Angery Toggled')
	print('Angery Mode Toggled')

#Hease Mode Toggle
@sheev.command()
async def hease():
	global heaseState
	heaseState = not heaseState
	await sheev.say('Hease Mode Toggled')
	print('Hease Mode Toggled')

#Checking For Stuff That Isn't A Command
@sheev.event
async def on_message(message):
	lowered_message = message.content.lower()
	if lowered_message.startswith('ping'):
		await sheev.send_message(message.channel, 'Pong!')
	if lowered_message.startswith('plop'):
		await sheev.send_message(message.channel, message.author.mention + ' Plop')
	if message.content.startswith('hello'): #Can't be lowered because 'Hello there' lowered starts with 'hello'
		await sheev.send_message(message.channel, 'Hello there, ' + message.author.mention)
	if 'autism' in message.content:
		await sheev.send_message(message.channel, message.author.mention + ' Autism has become an epidemic')
	if 'not coming on' in message.content or 'won\'t be on' in message.content:
		await sheev.send_message(message.channel, message.author.mention + ' REEEE WHY ARE YOU NEVER ON?!')
	if angeryState == True:
		await sheev.add_reaction(message, '😡')
	if heaseState == True:
		'''for x in sheev.get_all_emojis():
			if x.id == '310890946625667073':
				await sheev.add_reaction(message, x)'''
		await sheev.add_reaction(message, '<:hease:313427691338465281>')
	await sheev.process_commands(message)

#Function To Play Sound
async def playSound(track, user):
	channel = sheev.get_channel('210735188798341122')
	if(user in channel.voice_members):
		try:
			voice = await sheev.join_voice_channel(channel)
			player = voice.create_ffmpeg_player('C:\\Users\\Matthew\\Documents\\Discord Bots\\Sheev Bot\\SFX\\' + track + '.mp3')
			player.start()
			while True:
				if player.is_done():
					await voice.disconnect()
					print('Played ' + track)
					break
		except:
			await sheev.say("An error has occured, who knows what it was because I'm too lazy to code in each exception but probably just stop spamming it you skrub")
	else:
		await sheev.say("You can't play a sound effect unless you are in the channel you absolute normie")

#Text Responses
@sheev.command()
async def version(*args):
	await sheev.say("I am Sheev Bot v" + botversion + "\nI am the Senate!")
	print('Displayed Version')

@sheev.command()
async def changelog(*args):
	await sheev.say('''Changelog:
v0.1: Influenced the midichlorians to create... life
v0.2: Added many sounds, cleaned up spaghetti code
v0.3: Added roll the dice because why not
v0.4: Added Angery Mode and logging''')
	print('Displayed Changelog')
	
@sheev.command()
async def tragedy(*args):
	return await sheev.say("Did you ever hear the tragedy of Darth Plagueis The Wise? I thought not. It’s not a story the Jedi would tell you. It’s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself.")
	print('Told The Tragedy of Darth Plagueis The Wise')
	
@sheev.command()
async def rtd(lLimit_input, uLimit_input):
	try:
		lLimit = int(lLimit_input)
		uLimit = int(uLimit_input)
		rolled = random.randint(lLimit, uLimit)
		return await sheev.say(rolled)
		print('Rolled a dice between ' + lLimit_input + 'and ' + uLimit_input + 'and got ' + str(rolled))
	except:
		return await sheev.say("You broke it you idiot and I'm not sure why but probably because you tried to use words. Since when does a dice have words on?")

@sheev.command(pass_context=True)
async def stfu(ctx, user):
	await sheev.say(ctx.message.author.mention + ' says shut the fuck up ' + user)

@sheev.command(pass_context=True)
async def face(ctx):
	#textchannel = sheev.get_channel('277763238576259072')
	return await sheev.send_file(ctx.message.channel, 'SheevFace.jpg')
	print('Displayed a glorious picture of The Senate')
	
'''
@sheev.command()
async def yt(link):
	channel = sheev.get_channel('210735188798341122')
	voice = await sheev.join_voice_channel(channel)
	ytplayer = await voice.create_ytdl_player(link)
	ytplayer.start()
	while True:
		if ytplayer.is_done():
			await voice.disconnect()
			break
'''	
#Sound Responses
@sheev.command(pass_context=True)
async def boop(ctx):
	await playSound('Boop', ctx.message.author)

@sheev.command(pass_context=True)
async def dewit(ctx):
	await playSound('Dew It', ctx.message.author)

@sheev.command(pass_context=True)
async def happylanding(ctx):
	await playSound('Another Happy Landing', ctx.message.author)

@sheev.command(pass_context=True)
async def screech(ctx):
	await playSound('Autistic Screeching', ctx.message.author)
	
@sheev.command(pass_context=True)
async def generalkenobi(ctx):
	await playSound('General Kenobi', ctx.message.author)

@sheev.command(pass_context=True)
async def healing(ctx):
	await playSound('Healing', ctx.message.author)

@sheev.command(pass_context=True)
async def hello(ctx):
	await playSound('Hello There', ctx.message.author)

@sheev.command(pass_context=True)
async def senate(ctx):
	await playSound('I Am The Senate', ctx.message.author)

@sheev.command(pass_context=True)
async def sand(ctx):
	await playSound('I Don\'t Like Sand', ctx.message.author)

@sheev.command(pass_context=True)
async def sandF(ctx):
	await playSound('I Don\'t Like Sand Full', ctx.message.author)

@sheev.command(pass_context=True)
async def highground(ctx):
	await playSound('I Have The High Ground', ctx.message.author)

@sheev.command(pass_context=True)
async def treason(ctx):
	await playSound('It\'s Treason Then', ctx.message.author)

@sheev.command(pass_context=True)
async def excuse(ctx):
	await playSound('Jar Jar Exqueese Me', ctx.message.author)

@sheev.command(pass_context=True)
async def rude(ctx):
	await playSound('Jar Jar How Rude', ctx.message.author)

@sheev.command(pass_context=True)
async def back(ctx):
	await playSound('Jar Jar Meesa Back', ctx.message.author)

@sheev.command(pass_context=True)
async def ohno(ctx):
	await playSound('Jar Jar Oh No', ctx.message.author)

@sheev.command(pass_context=True)
async def smells(ctx):
	await playSound('Jar Jar That Smells', ctx.message.author)

@sheev.command(pass_context=True)
async def younglings(ctx):
	await playSound('Killing Younglings', ctx.message.author)

@sheev.command(pass_context=True)
async def liar(ctx):
	await playSound('Liar!', ctx.message.author)

@sheev.command(pass_context=True)
async def lmg(ctx):
	await playSound('LMG', ctx.message.author)

@sheev.command(pass_context=True)
async def toomany(ctx):
	await playSound('Master Skywalker With Lightsaber', ctx.message.author)

@sheev.command(pass_context=True)
async def masterwindu(ctx):
	await playSound('Master Windu', ctx.message.author)

@sheev.command(pass_context=True)
async def newempire(ctx):
	await playSound('My New Empire', ctx.message.author)

@sheev.command(pass_context=True)
async def no(ctx):
	await playSound('No', ctx.message.author)

@sheev.command(pass_context=True)
async def noot(ctx):
	await playSound('Noot Noot', ctx.message.author)

@sheev.command(pass_context=True)
async def normies(ctx):
	await playSound('Normies', ctx.message.author)

@sheev.command(pass_context=True)
async def notyet(ctx):
	await playSound('Not Yet', ctx.message.author)

@sheev.command(pass_context=True)
async def podracing(ctx):
	await playSound('Now This Is Podracing', ctx.message.author)

@sheev.command(pass_context=True)
async def potato(ctx):
	await playSound('Potato', ctx.message.author)

@sheev.command(pass_context=True)
async def shreck(ctx):
	await playSound('Shreck Hello', ctx.message.author)

@sheev.command(pass_context=True)
async def surprise(ctx):
	await playSound('Surprise', ctx.message.author)

@sheev.command(pass_context=True)
async def takeaseat(ctx):
	await playSound('Take A Seat', ctx.message.author)

@sheev.command(pass_context=True)
async def trust(ctx):
	await playSound('Trust', ctx.message.author)

@sheev.command(pass_context=True)
async def power(ctx):
	await playSound('Unlimited Power', ctx.message.author)

@sheev.command(pass_context=True)
async def yee(ctx):
	await playSound('Yee', ctx.message.author)

@sheev.command(pass_context=True)
async def yipee(ctx):
	await playSound('Yipee', ctx.message.author)

@sheev.command(pass_context=True)
async def arrest(ctx):
	await playSound('You Are Under Arrest Chancellor', ctx.message.author)

@sheev.command(pass_context=True)
async def lost(ctx):
	await playSound('You Have Lost', ctx.message.author)

@sheev.command(pass_context=True)
async def fast(ctx):
	select = random.randint(1,5)
	await playSound('Fast ' + str(select), ctx.message.author)

@sheev.command(pass_context=True)
async def fastF(ctx):
	select = random.randint(1,3)
	await playSound('Fast Full ' + str(select), ctx.message.author)

@sheev.command(pass_context=True)
async def nope(ctx):
	await playSound('Nope', ctx.message.author)

@sheev.command(pass_context=True)
async def hithere(ctx):
	await playSound('Hi There', ctx.message.author)

@sheev.command(pass_context=True)
async def play(ctx):
	await playSound('Julian Play', ctx.message.author)

@sheev.command(pass_context=True)
async def vsauce(ctx):
	await playSound('Vsauce Michael', ctx.message.author)

@sheev.command(pass_context=True)
async def retard(ctx):
	await playSound('Retard Alert', ctx.message.author)

@sheev.command(pass_context=True)
async def bighole(ctx):
	await playSound('Big Hole', ctx.message.author)

@sheev.command(pass_context=True)
async def nuts(ctx):
	await playSound('Nuts', ctx.message.author)

@sheev.command(pass_context=True)
async def getout(ctx):
	await playSound('Normies Get Out', ctx.message.author)

@sheev.command(pass_context=True)
async def yeehaw(ctx):
	await playSound('Yee Haw', ctx.message.author)

@sheev.command(pass_context=True)
async def bloodsugar(ctx):
	await playSound('Blood Sugar Spam', ctx.message.author)

@sheev.command(pass_context=True)
async def carameldansen(ctx):
	await playSound('CaramelDansen Ryu Remix', ctx.message.author)

@sheev.command(pass_context=True)
async def johncena(ctx):
	await playSound('John Cena', ctx.message.author)

@sheev.command(pass_context=True)
async def somebody(ctx):
	await playSound('Somebody Once Told Me', ctx.message.author)

@sheev.command(pass_context=True)
async def cyka(ctx):
	await playSound('Cyka Blyat', ctx.message.author)

sheev.run(token)