from discord.ext import commands
import requests
from urllib.parse import quote_plus
from random import randrange
import json
import html

class TruthorDare(commands.Cog):
  """Commands to handle truth or dare"""
  def __init__(self, bot):
    self.bot = bot
    self.truth_file = 'test_truth.txt'
    self.dare_file = 'test_dare.txt'

  def check_is_author_owner():
    def predicate(ctx):
      if ctx.message.author.id in ctx.bot.botOwners:
        return True
      raise ctx.bot.get_cog('CommandErrorHandler').OwnerError
    return commands.check(predicate)

  @commands.command(name='submit-truth')
  async def _submit_truth(self, ctx, arg=None):
    """Submits a truth

    Arguments:

    """
      if arg is None:
        await ctx.send('You need to provide a submission. Please enclose it in quotation marks.')
        return

      with open(self.test_truth, 'a') as file:
        file.write(html.escape(arg))

      await ctx.send('Submission received.')

  @commands.command(name='dump-truth')
  @check_is_author_owner()
  async def _dump_truth(self, ctx, arg=None):
    with open(self.test_truth, 'r') as file:
      dump = '```\n' + file.read() + '\n```'

    await ctx.send(dump)

  @commands.command(name='submit-dare')
  async def _submit_dare(self, ctx, arg=None):
    """Submits a dare

    Arguments:

    """
      if arg is None:
        await ctx.send('You need to provide a submission. Please enclose it in quotation marks.')
        return

      with open(self.test_dare, 'a') as file:
        file.write(html.escape(arg))

      await ctx.send('Submission received.')

  @commands.command(name='dump-dare')
  @check_is_author_owner()
  async def _dump_dare(self, ctx, arg=None):
    with open(self.test_dare, 'r') as file:
      dump = '```\n' + file.read() + '\n```'

    await ctx.send(dump)

def setup(bot):
  bot.add_cog(TruthorDare(bot))
