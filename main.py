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
  "olpa" : "Olpa means Where in Tulu",
  "amma" : "Amma means Mother in Tulu",
  "Daye" : "Daye means Why in Tulu"
}

eng_to_tulu = {
  "hello" : "Namaskara",
  "yes" : "Andh",
  "name" : "Pudhar",
  "cow" : "Petha",
  "chicken" : "Kori",
  "sad" : "Bejara",
  "happy" : "Kushi",
  "where" : "Olpa",
  "why" : "Daye",
  "how" : "Encha",
  "me" : "Yaan",
  "we" : "Namma",
  "hometown" : "Ooru",
  "home" : "Illa",
  "shop" : "Angadi",
  "good" : "Edde",
  "here" : "Mulpa",
  "one" : "Onji",
  "two" : "Rad",
  "three" : "Muji",
  "four" : "Naal",
  "five" : "Ain",
  "six" : "Aaji",
  "seven" : "Ale",
  "eight" : "Enma",
  "nine" : "Ormba",
  "ten" : "Path",
  "sugarcane" : "Curmb",
  "boy" : "Aan",
  "girl" : "Ponnu",
  "how are you" : "Yeer encha ullar?",
  "what are you doing" : "Dada malthond ullar"
}

sentences = ' { "what are you doing?" : "Yeer dada malthond ullar?", "what is your name?" : "Yeerna poodar dade?", "where are you from?" : "Yeerna oor olpa?", "how are you?" : "Yeer encha ullar", "i am fine" : "Yaan ushaari ulle" } ' 

load_sentences = json.loads(sentences);

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
async def translateword(ctx, args):
    guild = ctx.guild

    await ctx.send(eng_to_tulu[args])

@bot.command(pass_contezt=True)
async def translatesentence(ctx, *, arg):
    guild = ctx.guild

    await ctx.send(load_sentences[arg])
    
#client.run(os.getenv('TOKEN')
bot.run(os.getenv('TOKEN'))