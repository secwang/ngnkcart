import discord
import os
from discord.ext import commands
import sqlite3
from datetime import datetime, timedelta, timezone

def commit(str):
    BJ = timezone(timedelta(hours=+8), 'BJ')
    db = sqlite3.connect('table.sqlite3')
    ts = datetime.now(BJ).strftime('%Y-%m-%d %H:%M:%S')
    sql = f"INSERT INTO raw (time,str) VALUES ('{ts}', '{str}' );"
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close()


def search(key):
    db = sqlite3.connect('table.sqlite3')
    sql = f"select * from cart where NAME like '%{key}%' or DESCRIPTION like '%{key}%'"
    cursor = db.cursor()
    cursor.execute(sql)
    x =cursor.fetchone()
    db.close()
    return x

def count():
    db = sqlite3.connect('table.sqlite3')
    sql = f"select count(*) from cart"
    cursor = db.cursor()
    cursor.execute(sql)
    x =cursor.fetchone()[0]
    db.close()
    return x

bot = commands.Bot(command_prefix='>')

@bot.command()
async def kch(ctx):

    c = count()
    r = f'''cart:{c}
kch -> show help
kcs -> search in cart
kcc -> add your code to cart, need code,name,description, example
kcp -> table.tsv permalink
    '''
    await ctx.send(r)


@bot.command()
async def kcs(ctx,key):
    r = search(key)
    if r:
        await ctx.send(r)
    else:
        await ctx.send('Oops.Not found.')


@bot.command()
async def kcc(ctx):
    msg = ctx.message.content
    msg = msg[3:]

    r = commit(msg)
    await ctx.send('Added to log. waiting merge into cart.')

@bot.command()
async def kcp(ctx):
    await ctx.send('https://bit.ly/3MDQ4Zm')

token = os.getenv('NGNKCARTBOT_TOKEN')
bot.run(token)
