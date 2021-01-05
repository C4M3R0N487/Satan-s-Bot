import discord
import os
import json
from discord.ext import commands
from pretty_help import PrettyHelp

description = 'The KMLegion\'s own discord bot! Currently under construction!'
commandChar = "%"
# Intents can be used once things are fully set up. For now we don't need them.
intents = discord.Intents.default()
#intents.members = True
# Optional argument to pass in:
#help_command=PrettyHelp(dm_help=True, sort_commands=False, active_time=30)
bot = commands.Bot(command_prefix=commandChar, description=description, intents=intents)

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

bot.load_extension('extensions.retriever')
bot.load_extension('extensions.utils')
bot.load_extension('extensions.moderator')
bot.load_extension('extensions.helpers.errorhelper')
bot.load_extension('extensions.helpers.datahelper')
bot.load_extension('extensions.helpers.heartbeathelper')

bot.run(os.environ.get(str('BOT_TOKEN')))
