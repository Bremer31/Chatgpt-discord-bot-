
import discord
import openai

intents = discord.Intents.all()
intents.members = True
from  discord.ext import commands
bot = commands.Bot(command_prefix = "!",help_command=None,intents = intents) 
openai.api_key = "enter API Key"


@bot.command()
async def ping(context):
    await context.send("pong")
@bot.event
async def on_ready():
    print("bot is online")

@bot.event
async def on_message(message):
 
  if message.author == bot.user:
    return
  
  
  if bot.user in message.mentions:
 
   
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=f"{message.content}",
    max_tokens=2048,
    temperature=0.5,
    )

  # Send the response as a message
  await message.channel.send(response.choices[0].text)



bot.run("Enter Discord Token ")
