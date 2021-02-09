import asyncio
import motor.motor_asyncio
import os
from urllib.parse import quote_plus
from dotenv import load_dotenv
load_dotenv()

class DBAccessor(object):
  def __init__(self, dbs):
    dbkey = os.environ.get('DB_TOKEN')
    dburi = "mongodb://KMLBot:" + quote_plus(dbkey) + "@localhost:27017/?authSource=kml"
    del dbkey
    self._mongo = motor.motor_asyncio.AsyncIOMotorClient(dburi)
    self._db = self.mongo.kml

  async def cache_gif(self):
    self
