import discord
from discord.ext import commands
from discord.ext.commands.help import HelpCommand

class DaddyHelp(HelpCommand):
  """Custom implementation of the help command. Inspired by Mee6 help and pretty-help."""
  def __init__(self, **options):


    super().__init__(**options)
  
  async def prepare_help_command(self, ctx: commands.Context, command: commands.Command):
    if ctx.guild is not None:
      perms = ctx.channel.permissions_for(ctx.guild.me)
      if not perms.embed_links:
          raise commands.BotMissingPermissions(("embed links",))
      if not perms.read_message_history:
          raise commands.BotMissingPermissions(("read messahistory",))
    await super().prepare_help_command(ctx, command)