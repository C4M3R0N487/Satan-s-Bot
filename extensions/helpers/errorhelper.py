from discord.ext import commands

class CommandErrorHelper(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.OwnerError = self.owner_exception

  class owner_exception(commands.CommandError): pass
  
  @commands.Cog.listener()
  async def on_command_error(self, ctx, error):
    if hasattr(ctx.command, 'on_error'):
      return

    cog = ctx.cog

    if cog:
      if cog._get_overridden_method(cog.cog_command_error) is not None: return
    
    ignored = ()

    error = getattr(error, 'original', error)

    if isinstance(error, ignored):
      return

    if isinstance(error, commands.CommandNotFound):
      await ctx.send(ctx.bot.responses['CommandNotFound'])

    if isinstance(error, self.OwnerError):
      await ctx.send(ctx.bot.responses['OwnerError'])

def setup(bot):
  bot.add_cog(CommandErrorHelper(bot))