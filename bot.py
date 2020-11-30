import discord
from discord.ext import commands
import os
import time
import music_bot


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
    try:
        channel = ctx.author.voice.channel
        await channel.connect()
    except:
        pass
    for member in vc.members:
        print(member)
        impostor=str(member)
        print(impostor)
        if impostor !="Rythm#3722":
            await member.edit(mute=True) 
        else:
            print("haha jokes on you")
            

@client.command()
async def done(ctx):
    vc = ctx.author.voice.channel
    try:
        channel = ctx.author.voice.channel
        await channel.disconnect()
    except:
        pass
    for member in vc.members:
        await member.edit(mute=False)


@client.command()
async def play(ctx):
    await ctx.send("!p")

@client.command()
async def meet(ctx):
    vc = ctx.author.voice.channel
    try:
        channel = ctx.author.voice.channel
        await channel.disconnect()
    except:
        pass
    for member in vc.members:
        await member.edit(mute=False)
    time.sleep(145)
    await ctx.send("Lemme guess Shaajan was kicked?")
    try:
        channel = ctx.author.voice.channel
        await channel.connect()
    except:
        pass
    for member in vc.members:
        print(member)
        impostor=str(member)
        print(impostor)
        if impostor !="Rythm#3722":
            await member.edit(mute=True) 
        else:
            print("haha jokes on you")
        



client.run("TOKEN")
