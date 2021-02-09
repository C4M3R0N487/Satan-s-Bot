import discord
import os
import json
from discord.ext import commands
from pretty_help import PrettyHelp
from dotenv import load_dotenv
load_dotenv()
#import keyring
#import keyring_jeepney
#keyring.set_keyring(keyring_jeepney.Keyring())

description = 'The KMLegion\'s own discord bot! Currently under construction!'
commandChar = "%"
# Intents can be used once things are fully set up. For now we don't need them.
intents = discord.Intents.default()
#intents.members = True
# Optional argument to pass in:
#help_command=PrettyHelp(dm_help=True, sort_commands=False, active_time=30)
def prefix(bot, message):
  guild_key = message.guild.id
  if message.guild.id in bot.prefix_cache:
    return bot.prefix_cache[guild_key]
  else:
    return bot.extensions.datahelper.get_prefix(guild_key)
bot = commands.Bot(command_prefix=prefix, description=description, intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

bot.load_extension('extensions.retriever')
bot.load_extension('extensions.utils')
bot.load_extension('extensions.moderator')
bot.load_extension('extensions.helpers.errorhelper')
bot.load_extension('extensions.helpers.datahelper')
bot.load_extension('extensions.helpers.heartbeathelper')
bot.load_extension('extentions.truthordare')

bot.run(os.environ.get('BOT_TOKEN'))
