import os
import discord
from dotenv import load_dotenv
from maimai.user_data_fetch.add_friend import add_friend

load_dotenv()

bot = discord.Bot()


@bot.command(description="Maimai")
async def maimai_bot_register(ctx, friend_code: str):
    await ctx.respond('處理中，請稍後...')
    await ctx.send(f'{ctx.user.mention} \n {add_friend(ctx.user, friend_code)}')


@bot.command(description="獲取特定玩家資料")
async def get_user_data(ctx, friend_code: str = ''):
    await ctx.respond('處理中，請稍後...')


@bot.command(description="Testt")
async def t(ctx):
    await ctx.respond(f'{ctx.user.mention}')


bot.run(os.getenv("TOKEN"))
