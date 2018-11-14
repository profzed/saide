#Setup

import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

Client = discord.Client()
client = commands.Bot(command_prefix = "?")


#Say

@client.event
async def on_message(message):
    if message.content.upper().startswith('?SAY'):
       args = message.content.split(" ")
       await client.send_message(message.channel, "%s" % (" ".join(args[1:])))



#Welcome

@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Hello! I am Saide, and welcome!')
    print('Sent message to ' + member.name)


















#Token

client.run('NTA0OTMzMDY0NDczMDUxMTM2.DrMPyg.ovebYyiiEKfoeKiMWe6YyFHqP_8')
