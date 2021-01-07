import discord
from discord.ext import commands

class Utils(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self._last_member = None

  def check_is_author_owner():
    def predicate(ctx):
      if ctx.message.author.id in ctx.bot.botOwners:
        return True
      raise ctx.bot.get_cog('CommandErrorHandler').OwnerError
    return commands.check(predicate)

  @commands.command(name='peek')
  @check_is_author_owner()
  async def peek(self, ctx, arg):
    """Takes a peek at a part of the server.
    currently available: channel, channelid"""
    if arg == 'channel':
      await ctx.send(ctx.channel)
    elif arg == 'channelid':
      await ctx.send(ctx.channel.id)
    else:
      pass

  @commands.command(name='reloadext')
  @check_is_author_owner()
  async def _reloadExt(self, ctx, arg):
    extension = 'extensions.' + arg
    if extension in self.bot.extensions:
      self.bot.reload_extension(extension)
      await ctx.send('Reload successful.')
    else:
      await ctx.send('Extension not found.')

  @commands.command(name='dm')
  @check_is_author_owner()
  async def _dm_user(self, ctx, tgt, msg):
    """Takes a peek at a part of the server.
    currently available: channel, channelid"""
    target = ctx.message.mentions[0]
    await target.send(msg)

  @commands.command(name='echo')
  @check_is_author_owner()
  async def _echo(self, ctx, arg1: discord.TextChannel, arg2):
    await arg1.send(arg2)

def setup(bot):
  bot.add_cog(Utils(bot))
