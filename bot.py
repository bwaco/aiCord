import discord, openai_helper, json
from discord.ext import commands

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('!ask'):
        await message.reply(openai_helper.ask_openai(message.content[5:]))

bot.run(json.load(open('config.json'))['discord_token'])