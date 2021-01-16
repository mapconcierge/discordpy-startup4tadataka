from discord.ext import commands  # Bot Commands Frameworkをインポート
import os  # Python osモジュールをインポート tokenキーの取得で使用
import traceback  # 例外発生時の問題特定

bot = commands.Bot(command_prefix='忠敬さん')
token = os.environ['DISCORD_BOT_TOKEN']  # Heroku側にDISCORD_BOT_TOKEN変数としてTokenキーは記述してある


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

# メンテナンス用イベントハンドラ
@bot.command()
async def ping(ctx):
    await ctx.send('ぽん')

@bot.command()
async def map(ctx):
    await ctx.send('地図といえば伊能図じゃ！')


# 定型文イベントハンドラ
@bot.command()
async def 教えて(ctx):
    await ctx.send('日本地図学会の定期大会は2021年1月30日、31日の２日間、オンライン開催じゃ。')

@bot.command()
async def 助けて(ctx):
    tasukete_msg = '困ったときは ' + chr(35) + '総合受付 チャンネルに行くと誰かが助けてくれるぞ。'
    await ctx.send(tasukete_msg)

@bot.command()
async def はどう思う(ctx):
    await ctx.send('歩け歩け、続けることの大切さ。')

@bot.command()
async def そうですよね(ctx):
    await ctx.send('そのとおりです。')


  
bot.run(token)
