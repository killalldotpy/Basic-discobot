#!/usr/bin/env python3

import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Inloggad som {bot.user}')
    
    # Sätt status och aktivitet
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name="The Code"))
    
    # Här ersätter du 'KANAL_ID' med det riktiga ID för den kanal du vill skicka meddelandet till
    #channel = bot.get_channel(1143989469410770975)
    #if channel:
        #await channel.send('DrMössa!')
        
@bot.command()
async def type(ctx, *, text):
    await ctx.send(text)
        
bot.run('MTE0NTY3MjIwNDAzODcwMTA5OA.GgP1yz.-Y8RokC0g4MfACUHvdywPonV-YcmDURDy9Q2Zk')
