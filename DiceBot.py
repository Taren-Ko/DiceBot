#DiceBot by Cameron McCullers
#NOTE: IF YOU USE THIS BOT, YOU MUST PLACE YOUR BOT TOKEN INTO THE CODE AT THE END

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random

bot = commands.Bot(command_prefix='<>')

@bot.event
async def on_ready():
    print("This bot is running on " + bot.user.name +" with user ID " + bot.user.id)

@bot.command(pass_context=True)
async def cmdlist(ctx):
    await bot.say("Commands start with '<>'. Here is a list of them!")
    await bot.say("<>roll")


@bot.command(pass_context=True)
async def roll(ctx, die):
    dpos = die.find('d')
    if(dpos == -1):
        await bot.say("Dice commands must be of format 'int'd'int' (Ex. 3d20).\n Please try again.")
        return
    elif(dpos == 0):
        try:
            diceSize = int(die[1:])
        except ValueError:
            await bot.say("Dice commands must be of format 'int'd'int' (Ex. 3d20).\n Please try again.")
        await bot.say("You rolled a " + str(random.randint(1,diceSize)))
        return
    else:
        mult = die[:dpos]
        try:
            mult = int(mult)
        except ValueError:
            await bot.say("Dice commands must be of format 'int'd'int' (Ex. 3d20).\n Please try again.")
            return

        diceSize = die[dpos+1:]
        try:
            diceSize = int(diceSize)
        except ValueError:
            await bot.say("Dice commands must be of format 'int'd'int' (Ex. 3d20).\n Please try again.")
            return

        roll = random.randint(1,diceSize) * mult
        await bot.say("You rolled a " + str(roll))
        return
        


bot.run("PLACE BOT TOKEN HERE")