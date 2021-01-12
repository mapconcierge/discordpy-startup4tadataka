from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
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
    await ctx.send('地図じゃ！')

    
# 定期つぶやき
client = discord.Client() #インスタンス化

@client.event
async def on_ready():
    asyncio.ensure_future(greeting_gm())

async def greeting_gm():
    await client.send_message(channel, 'おはよう')
    await asyncio.sleep(60)
    
    
bot.run(token)
