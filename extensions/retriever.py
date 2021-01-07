from discord.ext import commands
import requests
from urllib.parse import quote_plus
from random import randrange
import json

class Retriever(commands.Cog):
  """Commands to retrieve media, quotes, etc"""
  def __init__(self, bot):
    self.bot = bot
    self._last_member = None

  def channel_is_porn_enabled(ctx):
    return ctx.channel.id in ctx.bot.pornChannels

  @commands.command(name='redgif')
  @commands.check(channel_is_porn_enabled)
  async def _rg_search(self, ctx, arg=None):
    """Returns a random gif from redgif based on search terms.

    Arguments:

    """
    numResults = 150
    if arg is None:
      await ctx.send(ctx.bot.responses['SearchArgs'])
      return

    response = requests.get('https://api.redgifs.com/v1/gfycats/search?search_text=' + quote_plus(arg) + '&count=' + str(numResults) + '&start=0')

    json_data = response.json()
    gfycats = json_data['gfycats']

    if len(gfycats) < 1:
      await ctx.send(ctx.bot.responses['NoGifsFound'])
    else:
      if numResults > len(gfycats):
        ran = len(gfycats)
      else:
        ran = numResults

      while(True):
        selector = randrange(ran)
        selection = gfycats[selector]
        """while "max5mbGif" not in selection:
          selector = randrange(ran)
          print(selector)
          selection = gfycats[selector]"""

        #selection = choice(gfycats)
        #print(selection)
        if 'max5mbGif' in selection:
          url = selection['max5mbGif']
          break
        elif 'max2mbGif' in selection:
          url = selection['max2mbGif']
          break
        elif 'mobileUrl' in selection:
          url = selection['mobileUrl']
          break
        elif 'max1mbGif' in selection:
          url = selection['max1mbGif']
          break
        else: continue
      print(url)
      await ctx.send(url)

  @commands.command(name='quote')
  async def _quote(self, ctx):
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + ' -' + json_data[0]['a'] + ' (Provided by <https://zenquotes.io> )'
    await ctx.send(quote)

  @_rg_search.error
  async def redgif_error(self, ctx, error):
    if isinstance(error, commands.CheckFailure):
      await ctx.send(ctx.bot.responses['NotAPornChannel'])


def setup(bot):
  bot.add_cog(Retriever(bot))
