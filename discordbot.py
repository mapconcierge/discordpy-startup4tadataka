from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='忠敬さん')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('ぽん')

@bot.command()
async def map(ctx):
    await ctx.send('地図といえば伊能図じゃ！')

@bot.command()
async def 教えて(ctx):
    await ctx.send('日本地図学会の定期大会は2021年1月30日、31日の２日間、オンライン開催じゃ。')

  
bot.run(token)
