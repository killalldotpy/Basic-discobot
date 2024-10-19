
import discord
from discord.ext import commands

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'Inloggad som {bot.user}')
    
    # Set status and message
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.listening, name="The Code"))
    

        
@bot.command()
async def type(ctx, *, text):
    await ctx.send(text)
        
bot.run('TOKEN')
