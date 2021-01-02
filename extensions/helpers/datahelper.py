from discord.ext import commands
import json
import config

class DataHelper(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

    with open('./responses.json') as file:
      response_data = json.load(file)
    self.bot.responses = response_data
    self.bot.botOwners = config.botOwners
    self.bot.pornChannels = config.pornChannels

def setup(bot):
  bot.add_cog(DataHelper(bot))