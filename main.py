import discord
import os
import requests
import json
import random
from discord.ext import commands
from discord.ext.commands import MissingPermissions

#client = discord.Client()
bot = commands.Bot(command_prefix = "!")

bad_words = ["bvc", "byawarsi"]

tuludict = {
  "namaskara" : "Namaskara means Hello in Tulu",
  "illa" : "Illa means House in Tulu",
  "yenchina" : "Yenchina means Why in Tulu",
  "olpa" : "Olpa means Where in Tulu"
}

eng_to_tulu = {
  "hello" : "Namaskara",
  "yes" : "Andh",
  "name" : "Pudhar",
  "cow" : "Petha",
  "chicken" : "kori",
  "sad" : "bejara",
  "happy" : "kushi"

}
warning_words = [
  "WARNING : Please refrain from profanity",
  "WARNING : Mulpa bad words allowed ijji"
]

@bot.event
async def on_ready():
  print("Namaskara {0.user}, ".format(bot))

@bot.event
async def on_message(message):
  if message.author == bot.user:
    return
 
  #await bot.process_commands(message)

  msg = message.content

  if msg.startswith('$hello'):
    await message.channel.send("Namaskara!")

  if any(word in msg for word in bad_words):
    await message.channel.send(random.choice(warning_words))

  await bot.process_commands(message)

#@bot.bot_has_guild_permissions(manage_channels=True)
@bot.command(pass_context=True)
async def createchannel(ctx, channelName):
    guild = ctx.guild

    embedvar = discord.Embed(
      title = 'Success',
      description = "{} has been successfully created!".format(channelName)
    )
    await guild.create_text_channel(name='{}'.format(channelName))
    await ctx.send(embed=embedvar)

@bot.command(pass_contezt=True)
async def definition(ctx, args):
    guild = ctx.guild

    await ctx.send(tuludict[args])
   #if any(word in args for word in tuludict.key()):
     #await ctx.send(tuludict.value)

@bot.command(pass_contezt=True)
async def translate(ctx, args):
    guild = ctx.guild

    await ctx.send(eng_to_tulu[args])
#client.run(os.getenv('TOKEN')
bot.run(os.getenv('TOKEN'))