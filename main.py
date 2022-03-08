import discord
import os

client = discord.Client()

TOKEN = os.environ['Token']
GUILD = os.environ['Guild']

@client.event
async def on_ready():
  for guild in client.guilds:
    if guild.name == GUILD:
      break

  print(
    f'{client.user} is connected to the following guild: \n'
    f'{guild.name}(id: {guild.id})\n'
  )

  members = '\n - '.join([member.name for member in guild.members])
  print(f'Guild Members:\n - {members}')


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('fuck'):
    await message.channel.send('We DONT use that type of language here')
    
  if message.content.startswith('shit'):
    await message.channel.send('We DONT use that type of language here')

  if message.content.startswith('cunt'):
    await message.channel.send('We DONT use that type of language here')

  if message.content.startswith('dick'):
    await message.channel.send('We DONT use that type of language here')

  if message.content.startswith('tit'):
    await message.channel.send('We DONT use that type of language here')

  if message.content.startswith('ass'):
    await message.channel.send('We DONT use that type of language here')
    

  if message.content.startswith('nigh'):
    await message.channel.send('I am here cause you started with the letters n-i-g, and I thought it was about to go a bad direction')
  elif message.content.startswith('nig'):
    await message.channel.send('That is just a hate crime. Figures, with so many white kids in here')
    
client.run(TOKEN)

            
            
