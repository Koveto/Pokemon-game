import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('ODg2MDQxMTg4MzkyNjUyODYx.YTv0KQ.Brbx-7gTYuYszuYm4ISRlE8b3xM')
