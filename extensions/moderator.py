from discord.ext import commands
from urllib.parse import quote_plus
from random import randrange
import discord
import json
import requests

class Moderator(commands.Cog):
  """Commands to manage roles, users, and messages"""
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_message(self, msg):
    """Listening when messages are sent"""
    if msg.channel.id == 766241115920924673:
      if msg.content.startswith('spmsg'):
        # Parse out the intro
        await self._parse_intro(msg)
  
  async def _parse_intro(self, msg):
    txt = msg.content.lower()
    parts = txt.split('\n')
    parts = parts[1:] # Remove this line before production!
    print(parts)
    for part in parts:
      if part.startswith('age:'):
        age = int(part[-2:])
      if part.startswith('name: '):
        name = part[7:]
      if 'weeniepeen' in part:
        codeword = True
    if age >= 18 and name and codeword is True:
      pending = discord.utils.get(msg.guild.roles, id=794463983209545779)
      approved = discord.utils.get(msg.guild.roles,   id=794464059126317106)
      await msg.author.remove_roles(pending)
      await msg.author.add_roles(approved)
      await msg.channel.send('You\'ve been approved!')
      


def setup(bot):
  bot.add_cog(Moderator(bot))