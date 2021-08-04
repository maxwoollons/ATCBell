from inspect import EndOfBlock
import discord
from discord.channel import VoiceChannel
from discord.client import Client
from discord.ext import commands, tasks
from discord.ext.commands.core import command
import datetime #need to install this on the live server
import json
import asyncio
from datetime import datetime
from discord.ext import commands
import time
import sched








client = commands.Bot(command_prefix = "=",description='I am a VoiceChannel Bot, DM Sand#4193 for assistance')



#cogs
cogs = []

for cog in cogs:
    try:
        client.load_extension(cog)
    except Exception as e:
        print(f'could not load cog {cog}: {str(e)}')


#-----------------------------------------------


client.remove_command("help")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    server_amt = len(client.guilds)
    listning = "for =help | " + str(server_amt) + " servers"
    # Setting `Listening ` status
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=listning))
    return



def p1():
    print('It is period one')





client.run('ODcyMzEwNjYzMTM2MDIyNTgw.YQoAnA.mMAeLWpQwd-GCSbFjCXQMBap2AQ')



#bell bot ODcyMzEwNjYzMTM2MDIyNTgw.YQoAnA.mMAeLWpQwd-GCSbFjCXQMBap2AQ

#dev = ODYzMDExOTkxMTAyOTQ3MzI4.YOgsjA.VTg4NdfSTg_ivGxhqUUCHyzFD24
#live = ODI2MDAyNzY0OTk1MTAwNzMy.YGGJBQ.DrTZuA9nSbskRgL2rAwQWlBkKfU