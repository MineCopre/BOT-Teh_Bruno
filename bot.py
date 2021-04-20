import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import videos

load_dotenv()


DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = discord.Client()
bot = commands.Bot(command_prefix="$")

#print("running")

@bot.command()
async def ping(ctx):
	await ctx.channel.send("pong")

async def video(ctx):
	await ctx.channel.send(file=discord.File(videos.get_random_video()))

bot.run(DISCORD_TOKEN)
