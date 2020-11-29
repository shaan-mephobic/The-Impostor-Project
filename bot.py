import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = ">")

@client.event
async def on_ready():
    print("Up And Runnin'!")

@client.command()
async def clear5(ctx, amount=6):
    await ctx.channel.purge(limit=amount)

@client.command()
async def clear3(ctx, amount=4):
    await ctx.channel.purge(limit=amount)

@client.command()
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)

@client.command()
async def whoisyourdaddy(ctx): 
    await ctx.send("Is that even a question? It's obviously \n shaan_mephobic")

client.run("NzgyNTQwOTQ0NDQ0MjI3NTk1.X8NsDA.SGDa_vlS2qKJCAMPKLgEXGQFjXA")