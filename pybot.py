import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Intents allow the bot to access certain information
intents = discord.Intents.default()

intents.message_content = True  # Required to read messages

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command()
async def hi(ctx):
    await ctx.send("Hello!")


@bot.command()
async def sup(ctx):
    await ctx.send("Im good, thanks!")

@bot.command()
async def bots(ctx):
    await ctx.send(f"{ctx.author} said bot {bots_count} times")
    

bots_count = 0

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    print(f"{message.author}: {message.content}")

    if message.content == "bot":
        await message.channel.send(f"Hello {message.author.display_name}! 👋")
        global bots_count
        bots_count += 1

    await bot.process_commands(message)

load_dotenv(dotenv_path="config/.env")
ticket = os.getenv("DISCORD_BOT_PYBOT")

bot.run(ticket)
