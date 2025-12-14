# Bit of nonsense for importing files, folders, and such.
import discord
from discord.ext import commands
import logging
from dotenv import load_dotenv
import os
import random

from keep_alive import keep_alive

# Discord Token is basically the bot's "account".
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

keep_alive()

# Logging for things the bot does (just in case), use for testing purposes, comment
# out when not testing.
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

# Intents are what the bot can do, commands refer to what commands can be given to
# the bot.
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Signify the bot is ready wherever it is being run.
@bot.event
async def on_ready():
    print(f"Bot \"{bot.user.name}\" is ready.")

# The only purpose this bot serves, to do RNG and spit out the results.
@bot.command()
async def mutate(ctx):
    # Initialize random seed.
    random.seed()

    # First check if any mutation happens, immediately ending if there is none.
    mutation = random.randint(1, 100)
    result_text = "No mutation this time."

    # If a mutation does occur, the bot will say which mutation occurred (based on the percentage chance
    # of a mutation occurring, note these values are hard-coded for simplicity and because I'm lazy).
    if mutation > 60:
        match mutation:
            case 61 | 62:
                result_text = "Your dinosaur is albino."
            case 63 | 64:
                result_text = "Your dinosaur is melanistic."
            case 65 | 66:
                result_text = "Your dinosaur is blind."
            case 67 | 68 | 69:
                result_text = "Your dinosaur has astigmatism."
            case 70 | 71:
                result_text = "Your dinosaur is deaf."

            case 72 | 73 | 74:
                result_text = "Your dinosaur is hard of hearing."
            case 75 | 76:
                result_text = "Your dinosaur is leucistic."
            case 77 | 78:
                result_text = "Your dinosaur is piebald."
            case 79:
                result_text = "Your dinosaur has polydactyly."
            case 80:
                result_text = "Your dinosaur has oligodactyly."

            case 81:
                result_text = "Your dinosaur has chimerism."
            case 82 | 83:
                result_text = "Your dinosaur has erythrism."
            case 84 | 85:
                result_text = "Your dinosaur has xanthochromism."
            case 86 | 87:
                result_text = "Your dinosaur has dilution."
            case 88 | 89:
                result_text = "Your dinosaur has heterochromia."

            case 90:
                result_text = "Your dinosaur has gynandromorphism."
            case 91:
                result_text = "Your dinosaur has dwarfism."
            case 92 | 93:
                result_text = "Your dinosaur has axanthism."
            case 94 | 95:
                result_text = "Your dinosaur has monochromacy."
            case 96:
                result_text = "Your dinosaur has double pupils."

            case 97 | 98:
                result_text = "Your dinosaur has vitiligo."
            case 99 | 100:
                result_text = "Your dinosaur has hyperpigmentation."
            case _:
                result_text = "Error: match case invalid value (let's assume your dinosaur did not survive birth)"

    # Display the results of the RNG.
    await ctx.send(f"{result_text}")

# Run the bot when this file is actually ran.
bot.run(token)