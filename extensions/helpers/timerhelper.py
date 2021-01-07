from discord.ext import tasks, commands
import requests

class TimerHelper(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
    self.heartbeat.start()

  def cog_unload(self):
    self.heartbeat.cancel

  @tasks.loop(hours=4.0)
  async def tmr_four_hour(self):
    pass

  @tasks.loop(hours=12.0)
  async def tmr_twelve_hour(self):
    pass
