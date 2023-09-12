import os
import discord
from dotenv import load_dotenv

load_dotenv()

bot = discord.Bot()


@bot.command(description="Maimai")
async def maimai_bot_register(ctx):
    await ctx.respond(f"Hello {ctx.author.name}!")


bot.run(os.getenv("TOKEN"))
