import random
import time
import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio


Client = discord.Client()
client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print("Hello discord-chan")
    
@client.event
async def on_message(message):
    if message.content == "pacito":
        await client.send_message(message.channel, "May I please suck your weiner-kun oni-chan")
    elif message.content == "hello":
        await client.send_message(message.channel, "Hello oniii-chaan")
    elif message.content == "hi":
        await client.send_message(message.channel, "OWO")
    elif message.content == "is this loss":
        await client.send_message(message.channel, "I lost my pink dildo")
    elif message.content == "nigga":
        await client.send_message(message.channel, "whiten't")
    elif message.content == "sure":
        await client.send_message(message.channel, "I was kidding")
    elif message.content == "you suck":
        await client.send_message(message.channel, "U r mean :(")
    elif message.content == "DAMN":
        await client.send_message(message.channel, "y u angwy oni-chan OWO")
    elif message.content == "no u":
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Fuckin' NORMIE" %(userID))
    elif message.content == "send bob":
        await client.send_message(message.channel, "https://upload.wikimedia.org/wikipedia/en/thumb/c/c5/Bob_the_builder.jpg/220px-Bob_the_builder.jpg")
    elif message.content == "no":
        await client.send_message(message.channel, "Y NOT -o-")
    elif message.content == "yes":
        await client.send_message(message.channel, "ok ;P")
    elif message.content == "hi Hatsune Miku":
        await client.send_message(message.channel, "owoowowowowowo hiiiiiiiiiiiii")
    elif message.content == "!help":
        await client.send_message(message.channel, "Keywords: pacito, hi, hello, is this loss, nigga, sure, you suck, DAMN, no u, send bob, no, yes, hi Hatsune Miku")
    elif message.content == "it's gay":
        await client.send_message(message.channel, "grrrrr")

client.login(process.env.BOT_TOKEN);
