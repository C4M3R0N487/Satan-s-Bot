from discord.ext import commands
from pathlib import Path
from urllib.parse import quote_plus
import os
import json
import config
import motor.motor_asyncio

class DataHelper(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    dbkey = os.environ.get('DB_TOKEN')
    dburi = "mongodb://%s:%s@localhost:27017" % (quote_plus("AdminKira"), quote_plus(dbkey))
    self.mongo = motor.motor_asyncio.AsyncIOMotorClient(dburi)

    p = Path('/home/kira/kml/KMLegion-Bot/responses.json')
    with p.open() as file:
      response_data = json.load(file)
    self.bot.responses = response_data
    self.bot.botOwners = config.botOwners
    self.bot.pornChannels = config.pornChannels

def setup(bot):
  bot.add_cog(DataHelper(bot))
