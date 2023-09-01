import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='>')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run('ODg2MDQxMTg4MzkyNjUyODYx.YTv0KQ.Brbx-7gTYuYszuYm4ISRlE8b3xM')
