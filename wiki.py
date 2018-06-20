import discord
import math
import os
from discord.ext import commands
from discord.ext.commands import Bot

Bot = discord.Client()
bot = commands.Bot(command_prefix='$')
sellValueOne = 0.25
sellValueTwo = 0.90

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.lower().startswith('$sellback'):
        args = message.content.split(" ")
        if len(args) == 3:
           price = args[1].replace(',','')
           currency = args[2]
           if price.isdigit() is True and int(price) >= 0:
               if currency.lower() == 'gold':
                   goldSell = int(price) * sellValueOne
                   await bot.send_message(message.channel, '{:,} Gold'.format(math.ceil(goldSell)))
               elif currency.lower() == 'ac':
                   acSellFirst = int(price) * sellValueTwo
                   acSellSecond = int(price) * sellValueOne
                   await bot.send_message(message.channel, 'First 24 Hours: {:,} AC'.format(math.ceil(acSellFirst)))
                   await bot.send_message(message.channel, 'After 24 Hours: {:,} AC'.format(math.ceil(acSellSecond)))
               else:
                   await bot.send_message(message.channel, 'Please indicate if the item is AC or Gold.')
           else:
               await bot.send_message(message.channel, 'Please enter a valid non-zero, non-negative number.')
        else:
            await bot.send_message(message.channel, 'Please use the syntax: **$sellback <price> <AC/Gold>**')

    if message.content.lower().startswith('$aqwchar'):
        charLook = message.content.split(' ')
        char = charLook[1:]
        if len(char) > 0:
            await bot.send_message(message.channel, '{}{}'.format('Link: http://www.aq.com/character.asp?id=', '%20'.join(char[0:])))
        else:
            await bot.send_message(message.channel, 'Please specify a name after $aqwchar')

    if message.content.lower().startswith('$wiki'):
        query = message.content.split(' ')
        search = query[1:]
        search = [item.replace('+','') for item in search]
        if len(search) > 0:
            await bot.send_message(message.channel, '{}{}'.format('Wiki search: http://aqwwiki.wikidot.com/search:site/q/', '+'.join(search[0:])))
        else:
            await bot.send_message(message.channel, 'Please specify what you want to search after !wiki')

    if message.content.lower().startswith('$3dchar'):
        charLook = message.content.split(' ')
        char = charLook[1:]
        if len(char) > 0:
            await bot.send_message(message.channel, '{}{}'.format('Link: https://game.aq3d.com/account/Character?id=', '%20'.join(char[0:])))
        else:
            await bot.send_message(message.channel, 'Please specify a name after $3dchar')

    if message.content.lower().startswith('$3dwiki'):
        query = message.content.split(' ')
        search = query[1:]
        if len(search) > 0:
            await bot.send_message(message.channel, '{}{}'.format('Wiki search: http://aq-3d.wikidot.com/search:site/q/', '%20'.join(search[0:])))
        else:
            await bot.send_message(message.channel, 'Please specify what you want to search after !3dwiki')


@bot.event
async def on_ready():
    print('Bot is ready')

bot.run(os.environ['BOT_TOKEN'])
