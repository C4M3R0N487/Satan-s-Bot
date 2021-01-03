@bot.event
async def on_message(message):
    if message.author == client.user:
        return

    # we will concern ourselves with the string inside the message for the next section. This will become it's own method.
    content = message.content.lower()

    if content.startswith(commandChar + 'quote'):
      quote = get_quote()
      await message.channel.send(quote)

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

    @commands.Cog.listener()
    async def on_message(self, msg):
      """Automatically approves a user based on their message meeting certain requirements"""
      if msg.channel.id == 766241115920924673:
        txt = msg.content.lower()
        if 'age' in txt and 'name' in txt and 'weeniepeen' in txt:
          pending = discord.utils.get(msg.guild.roles, id=794463983209545779)
          approved = discord.utils.get(msg.guild.roles,   id=794464059126317106)
          await msg.author.remove_roles(pending)
          await msg.author.add_roles(approved)
          await msg.channel.send('You\'ve been approved!')



response = await requests.get('google.com')
if response:
  print('Got response from google.com')
else:
  print('Couldn\'t get a response during heartbeat!')
