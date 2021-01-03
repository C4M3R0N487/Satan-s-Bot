from discord.ext import commands
from pathlib import Path
import json
import config

class DataHelper(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

    p = Path('../../responses.json')
    with p.open() as file:
      response_data = json.load(file)
    self.bot.responses = response_data
    self.bot.botOwners = config.botOwners
    self.bot.pornChannels = config.pornChannels

def setup(bot):
  bot.add_cog(DataHelper(bot))
