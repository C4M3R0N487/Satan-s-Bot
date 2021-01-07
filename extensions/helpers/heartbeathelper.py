from discord.ext import tasks, commands
import time
import requests

class HeartbeatHelper(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.hb_delay = 30.0
    self.heartbeat.start()

  def cog_unload(self):
    self.heartbeat.cancel

  @tasks.loop(minutes=30.0)
  async def heartbeat(self):
    print('Heartbeat!')
    await self._check_sync()


  @heartbeat.before_loop
  async def before_heartbeat(self):
    print('waiting for startup...')
    await self.bot.wait_until_ready()
    print('waiting finished! Ready to go!')

  def check_is_author_owner():
    def predicate(ctx):
      if ctx.message.author.id in ctx.bot.botOwners:
        return True
      raise ctx.bot.get_cog('CommandErrorHandler').OwnerError
    return commands.check(predicate)

  @commands.command(name='chb', hidden=True)
  @check_is_author_owner()
  async def _change_heartbeat(self, ctx, arg=None):
    """Updates the delay between heartbeat/keepalive beats"""

    if arg is None:
      await ctx.send('Please provide an argument! (in number of minutes)')
    self.hb_delay = float(arg)
    self.heartbeat.change_interval(seconds=self.hb_delay)
    await ctx.send('Heartbeat interval changed.')

  @commands.command(name='stophb', hidden=True)
  @check_is_author_owner()
  async def _stop_heartbeat(self, ctx, arg=None):
    """Cancels the heartbeat/keepalive beats"""
    self.heartbeat.cancel()
    await ctx.send('Heartbeat stopped.')

  @commands.command(name='starthb', hidden=True)
  @check_is_author_owner()
  async def _start_heartbeat(self, ctx, arg=None):
    """Startss the heartbeat/keepalive beats"""
    self.heartbeat.start()
    await ctx.send('Heartbeat starting...')

  @_start_heartbeat.error
  async def start_error(self, ctx, error):
    if isinstance(error, RuntimeError):
      await ctx.send('Heartbeat is already running!')

  async def _check_sync(self):
    gmt = time.gmtime()
    if gmt[4] != 0 | 30:
      print('Time out of sync')
    else:
      print('Time in sync')

def setup(bot):
  bot.add_cog(HeartbeatHelper(bot))
