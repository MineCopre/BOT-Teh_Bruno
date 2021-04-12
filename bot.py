import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()


DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

bot = discord.Client()
bot = commands.Bot(command_prefix="$")

@bot.command()
async def ping(ctx):
	await ctx.channel.send("pong")

bot.run(DISCORD_TOKEN)
