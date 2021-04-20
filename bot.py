import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import gifs
import says
import helper

load_dotenv()


DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = discord.Client()
bot = commands.Bot(command_prefix="$")

#print("running")

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
async def ajuda(ctx):
	await ctx.channel.send(embed=helper.help())

@bot.command()
async def equipa(ctx):
	await ctx.channel.send(embed=helper.team())

bot.run(DISCORD_TOKEN)
