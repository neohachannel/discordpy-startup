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
async def おやす(ctx):
    await ctx.send('おやすみなさい！！')

@bot.command()
async def HPB(ctx):
    await ctx.send('お誕生日おめでとうございます！！')

citycode = '016010'
resp = urllib.request.urlopen('http://weather.livedoor.com/forecast/webservice/json/v1?city=%s'%citycode).read()
resp = json.loads(resp.decode('utf-8'))

@client.event
async def on_ready():
  print("logged in as " + client.user.name)

@client.event
async def on_message(message):
  if message.author != client.user:

    if message.content == "Bot君、札幌の天気は？":
      msg = resp['location']['city']
      msg += "の天気は、\n"
      for f in resp['forecasts']:
        msg += f['dateLabel'] + "が" + f['telop'] + "\n"
      msg += "です。"

      await client.send_message(message.channel, message.author.mention + msg)

bot.run(token)
