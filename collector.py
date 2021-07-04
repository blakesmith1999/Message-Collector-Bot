import discord
import sys
import os

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='$')

@bot.command(name='mod')
async def add_mod(ctx, *args):
    await ctx.send('Saved to suggestion list!')
    file = open('mods.txt', 'a')
    #arg = args[5:]
    msg = ''.join(args)
    file.write(msg + '\n')
    file.close
    
@bot.command(name='list')
async def print_list(ctx):
    file = open('mods.txt')

    if os.stat('mods.txt').st_size == 0:
        await ctx.send('The list is empty.')

    else:
        await ctx.send('Listing mods')
        for x in file:
            await ctx.send(x)
    file.close()

async def clear_list(ctx, arg:str):
    if 'clear' in arg:
        await ctx.send('Mods list cleared')
        file = open('mods.txt', "w")
        file.write("")
        file.close()


@bot.command(name='restart')
async def restart_bot(ctx):
    await ctx.bot.close()
    await bot.start(TOKEN, bot=True)

@bot.command(name='stop')
async def stop_bot(ctx):
    await ctx.bot.close()


bot.run(TOKEN)