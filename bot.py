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
async def stfu(ctx): 
    await ctx.send("Yo Shaajan Why can't you just Shut the Fuck Up!")

@client.command()
async def game(ctx):
    vc = ctx.author.voice.channel
    for member in vc.members:
        print(member)
        if member !="Rythm#3722":
            await member.edit(mute=True)
                   
            
    
@client.command()
async def done(ctx):
    vc = ctx.author.voice.channel
    for member in vc.members:
        await member.edit(mute=False)



client.run("")
