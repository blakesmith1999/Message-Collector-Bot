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
    msg = args[5:]
    file.write(msg + '\n')
    file.close
    
@bot.command(name='list')
async def print_list(ctx, *args):
    if len(args) == 0:
        await ctx.send('Listing mods')
        file = open('mods.txt')
        await ctx.send(file.read())
    if args == 'clear':
        await ctx.send('Mods list cleared')
        os.remove('mods.txt')

@bot.command(name='stop')
async def stop_bot(ctx):
    await ctx.bot.logout()
    await login(TOKEN, bot=True)


bot.run(TOKEN)