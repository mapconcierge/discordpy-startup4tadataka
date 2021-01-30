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
async def はじまりましたね(ctx):
    await ctx.send('この２日間、オンライン大会を私も楽しみますよ。')

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

@bot.command()
async def お元気ですね(ctx):
    await ctx.send('当年276才。まだまだ元気ですよ！')

@bot.command()
async def 間宮さんについてどう思う(ctx):
    await ctx.send('間宮林蔵君には、わたしが果たせなかった北蝦夷を調べてもらい、助かっています。')

@bot.command()
async def 赤水さんについてどう思う(ctx):
    await ctx.send('長久保赤水先輩の地図が、にわかに話題になってきましたが、よろこばしいですね。')

@bot.command()
async def 生まれはどこ(ctx):
    await ctx.send('延享2年に上総国山辺郡小関村の名主「小関家」の子として生まれまして、「三次郎」と呼ばれていましたね。')

@bot.command()
async def どうして地図を作ったの(ctx):
    await ctx.send('歴学を学んでいるうちに、どうしても地球の大きさを知る必要があると思いまして、ただそのためには天体測量で遠くまで行かなければならず、一番遠い蝦夷まで測量しようと思いましたね。')

@bot.command()
async def おはようございます(ctx):
    await ctx.send('おはようございます。今日も元気に地図を作っていきましょう。')

@bot.command()
async def おつかれさまでした(ctx):
    await ctx.send('楽しく聴かせてもらいました。日本地図学会の発展をいつでも見守っていますよ。みなさんおつかれさまでした。')

@bot.command()
async def 本日はよろしくお願いいたします(ctx):
    await ctx.send('沢山の発表楽しみですね。')
    
@bot.command()
async def 緊張してきました(ctx):
    await ctx.send('わたしは旅に出る前、必ず富岡八幡宮さんにお参りしていましたよ。深呼吸してまずは落ち着きましょう。')


  
bot.run(token)
