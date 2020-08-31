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

インポート 要求
 urllibをインポートします。リクエスト
 BS4の インポート BeautifulSoup

インポート get_shortenURL

def  get_yahoo_news（）：
    ＃ヘッドラインニュースのタイトル格納用リスト
    news_data  = []

    ＃urlの指定
    url  =  'http://www.yahoo.co.jp/'

    ＃ユーザーエージェントを指定
    ua  =  'Mozilla / 5.0（Windows NT 10.0; WOW64; rv：60.0）' \
     'AppleWebKit / 537.36（KHTML、like Gecko）' \
     「Gecko / 20100101 Firefox / 60.0」

    req  =  urllib。リクエスト。リクエスト（url、headers = { 'User-Agent'：ua }）

    #htmlの取得
    html  =  urllib。リクエスト。urlopen（REQ）

    ＃htmlパース
    soup  =  BeautifulSoup（html、"html.parser"）
    topicsindex  =  soup。検索（'section'、attrs = { 'id'：'tabpanelTopics1' }）
    ＃class「topicsindex」内から記事タイトルを抽出
    li  =  topicsindex。find_all（'記事'）
    以下のために 私 にある 範囲（8）：
        a  =  li [ i ]。検索（'a'）
        b  =  li [ i ]。見つける（'スパン'）
        ＃記事タイトルとURLを保存
        url2  =  a。get（'href'）
        req2  =  urllib。リクエスト。リクエスト（url2、headers = { 'User-Agent'：ua }）
        html2  =  urllib。リクエスト。urlopen（req2）
        soup2  =  BeautifulSoup（html2、"html.parser"）
        topicsindex2  =  soup2。検索（class_ = 'pickupMain_articleSummary'）
        re_url  =  '-<' + get_shortenURL。get_shortenURL（。取得（'HREF'を））+ '> - '
        
        news_data。追加（[ b。コンテンツ [ 0 ]、topicsindex2。コンテンツ [ 0 ]、re_url ]）
    リターン news_data

def  get_nhk_news（）：
    ＃ニュース格納用リスト
    news_data  = []
    ＃urlの指定
    url  =  'http://k.nhk.jp/knews/index.html'

    ＃ユーザーエージェントを指定
    ua  =  'Mozilla / 5.0（Windows NT 10.0; WOW64; rv：60.0）' \
     'AppleWebKit / 537.36（KHTML、like Gecko）' \
     「Gecko / 20100101 Firefox / 60.0」

    req  =  urllib。リクエスト。リクエスト（url、headers = { 'User-Agent'：ua }）

    #htmlの取得
    html  =  urllib。リクエスト。urlopen（REQ）
    ＃htmlパース
    soup  =  BeautifulSoup（html、"html.parser"）
    ＃標準型NHKnewsのURLを取得したいときはこっち
    「」
    ＃標準型NHKnewsへの変換
    news_path = 'https://www3.nhk.or.jp/news/html/'
    all_a = soup.find_all（ 'a'）
    all_a = all_a [：7]
    （all_a）のインデックス：
        n_url = news_path + index.get（ 'href'）
        news_data.append（[index.contents [0]、n_url]）
    「」
    ＃軽く中身だけを表示したいときはこっち
    ＃簡易型NHKnewsへの変換
    text_data  = []
    long_path  =  'https://www3.nhk.or.jp/news/html/'
    news_path  =  'http://k.nhk.jp/knews/'
    all_a  =  soup。find_all（'a'）
    all_a  =  all_a [：7 ]
    ＃対象のURLを獲得
    以下のための 指数 で（all_aという）：
        n_url  =  news_path + index。get（'href'）
        l_url  =  long_path + index。get（'href'）
        news_data。追加（[ インデックス。コンテンツ [ 0 ]、n_url、l_url ]）
    以下のための データ で news_data：
        url  =  data [ 1 ]
        req  =  urllib。リクエスト。リクエスト（url、headers = { 'User-Agent'：ua }）
        #htmlの取得
        html  =  urllib。リクエスト。urlopen（REQ）
        ＃htmlパース
        soup  =  BeautifulSoup（html、"html.parser"）
        #title取得
        title_text  =  data [ 0 ]
        split_text  =  soup。テキスト。分割（" \ n "）
        以下のための 標的 で 範囲（LEN（split_text））。
            もし（split_text [ 対象 ]。見つけ（"" ）！= - 1）：
                main_text  =  split_text [ ターゲット ]
                date_text  =  split_text [ target + 2 ] + \
                    '-<' + get_shortenURL。get_shortenURL（data [ 2））+ '>-'
        text_data。追加（[ title_text、main_text、date_text、"-----" ]）
        ＃time.sleep（1）
        印刷（"*"）
    印刷（"-----"）
    リターン text_data、news_data


if  __name__  ==  '__main__'：
    get_yahoo_news（）

bot.run(token)
