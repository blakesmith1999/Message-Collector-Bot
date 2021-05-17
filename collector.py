import discord
from discord.ext import commands

TOKEN="ODQzODg1NTM1ODAxNjM4OTEz.YKKXpg.bHXhIA4cIHDow2jhBucb3QECeac"

bot = commands.Bot(command_prefix='$')

@bot.command(name='mod')
async def add_mod(ctx, *args):
    await ctx.send('Saved to suggestion list!')
    file = open('mods.txt', 'a')
    msg = args[5:]
    file.write(msg + '\n')
    file.close
    
@bot.command(name='list')
async def print_list(ctx):
    await ctx.send('Listing mods')
    file = open('mods.txt')
    await ctx.send(file.read())


bot.run(TOKEN)