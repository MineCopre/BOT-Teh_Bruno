import discord
import os
import sudo
from discord.ext import commands
import gifs
import says
import helper
import re


DISCORD_TOKEN = os.getenv("BOTBRUNODISCORDTOKEN")


bot = discord.Client()
bot = commands.Bot(command_prefix="$")
spamKeyWordsList = ["3 MONTHS:", "3 MONTHS", "3 month", "NITRO", "DISCORD", "GIFT", "GIFTS", "STEAM"]

@bot.event
async def on_message(message):
    
	spamNumber = 0
	messageUpper = message.content.upper()

	regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    
	url = re.findall(regex,message.content)

	if len(url) > 0:
		spamNumber += 2
	for x in spamKeyWordsList:
		if x in messageUpper:
			spamNumber = spamNumber + 1;
	if spamNumber >= 5:
		await message.delete()

		##Get logs channel and report spam
		logsChannel = bot.get_channel(818279209255305216)
		await logsChannel.send("Spam detetado e apagdo em " + message.channel.name+ " , enviado por " + message.author.display_name)
	else:
		await bot.process_commands(message)

@bot.command()
async def ping(ctx):
	await ctx.channel.send("*pong*, **pong**, ***pong***")

@bot.command()
async def jjgif(ctx):
	print("Got Command: jjgif")
	gif = gifs.get_random_gif()
	await ctx.channel.send(gif)

@bot.command()
async def jjdiz(ctx):
	print("Got Command: jjdiz")
	say = says.get_random_say()
	e = discord.Embed(title="JJ Diz:", description=say, color=0x5C5CFF)
	e.set_image(url=says.get_random_img())
	await ctx.channel.send(embed=e)

@bot.command()
async def apaga(ctx):
    print(ctx)

@bot.command()
async def ajuda(ctx):
	await ctx.channel.send(embed=helper.help())

@bot.command()
async def equipa(ctx):
	await ctx.channel.send(embed=helper.team())

#sudo.setup(bot)
bot.run(DISCORD_TOKEN)
    
