from discord.ext import commands
from pathlib import Path
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os
import json
import config
import asyncio
import motor.motor_asyncio
load_dotenv()
#import keyring
#import keyring_jeepney
#keyring.set_keyring(keyring_jeepney.Keyring())

class DataHelper(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    dbkey = os.environ.get('DB_TOKEN')
    dburi = "mongodb://KMLBot:" + quote_plus(dbkey) + "@localhost:27017/?authSource=kml"
    del dbkey
    self.mongo = motor.motor_asyncio.AsyncIOMotorClient(dburi)
    self.db = self.mongo['kml']

    self.bot.prefix_cache = {}

    p = Path('/home/kira/kml/KMLegion-Bot/responses.json')
    with p.open() as file:
      response_data = json.load(file)
    self.bot.responses = response_data
    self.bot.botOwners = config.botOwners
    self.bot.pornChannels = config.pornChannels

  async def get_prefix(self, guild_key):
    cache = self.bot.prefix_cache
    #prefs = await self.db.server_preferences.find_one({'_id': {'$eq': guild_key}})
    #if prefs:
    #  cache[guild_key] = prefs.prefix
    #  return prefs.prefix
    #else:
    #  cache[guild_key] = '%'
    #  return '%'
    cache[guild_key] = '%'
    return cache[guild_key]

def setup(bot):
  bot.add_cog(DataHelper(bot))
