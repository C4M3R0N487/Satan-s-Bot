from discord.ext import commands
from bs4 import BeautifulSoup
from urllib.parse import quote_plus
from random import randrange
import json
import aiohttp
import asyncio

class SoupHelper(object):
  """Commands to scrap websites"""
  def __init__(self, keywords=[], *args):
      self.keywords = keywords
      
