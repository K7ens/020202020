import discord
import os
 
client = discord.Client()
 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
 
@client.event
async def on_message(message):
    if message.author == client.user:
        return
 
    if message.content.startswith('Привет'):
        await message.channel.send('Здарова!')
    if message.content.startswith('пока'):
        await message.channel.send('Ага давай!')
 
client.run(ODM4MDM1NzkxNzg3MzI3NTYw.YI1Ppg.912NC9tMqgJGOYEOqTpMNUFeXUc)