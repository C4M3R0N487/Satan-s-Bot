from discord.ext import commands
from pathlib import Path
from urllib.parse import quote_plus
import os
import json
import config
import motor.motor_asyncio
import keyring
import keyring_jeepney
keyring.set_keyring(keyring_jeepney.Keyring())

class DataHelper(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    dburi = "mongodb://AdminKira:" + quote_plus(keyring.get_password("system", "AdminKira")) + "@localhost:27017"
    self.mongo = motor.motor_asyncio.AsyncIOMotorClient(dburi)

    p = Path('/home/kira/kml/KMLegion-Bot/responses.json')
    with p.open() as file:
      response_data = json.load(file)
    self.bot.responses = response_data
    self.bot.botOwners = config.botOwners
    self.bot.pornChannels = config.pornChannels

def setup(bot):
  bot.add_cog(DataHelper(bot))
