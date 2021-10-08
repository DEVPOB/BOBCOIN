from asyncio.tasks import wait_for
from typing import Text
import warnings
import discord
import random
import asyncio
from datetime import date, datetime, time,timedelta
from discord import message
from discord import client
from discord import member
from discord.flags import Intents, alias_flag_value
import requests
from bs4 import BeautifulSoup
from discord.ext import commands
import json
import os
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import discord

Intents = discord.Intents.default()
Intents.members = True

url = 'https://www.imdb.com/chart/top'

os.chdir(r'C:\Users\My PC\Desktop\discord-bot\discord-bot')


message_lastseen = datetime.now()
bot = commands.Bot(command_prefix = '$')
botrandom = random.randint(0,2)
botimage = ['https://logos-world.net/wp-content/uploads/2020/12/Discord-Logo.png','https://image.flaticon.com/icons/png/512/124/124010.png',\
    'https://upload.wikimedia.org/wikipedia/commons/thumb/0/09/YouTube_full-color_icon_%282017%29.svg/640px-YouTube_full-color_icon_%282017%29.svg.png']
@bot.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandNotFound):
        await ctx.send("ไม่มีคำสั่งนี้")
@bot.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandOnCooldown):
        msg = '**ไอสัสใจเย็น**  ลองอีกครั้งอีก{:.2f}วิ'.format(error.retry_after)
        await ctx.send(msg)

@bot.command()
async def stonk(ctx, user: discord.Member = None):
    if user == None:
        user = ctx.author
    rich = Image.open("pic.jpg")
    asset = user.avatar_url_as(size = 128)
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp = pfp.resize((177,177))
    rich.paste(pfp,(342,0))
    rich.save("picture.jpg")
    await ctx.send(file = discord.File("picture.jpg"))

@bot.command()
async def DTC(ctx,*,text = "No text entered"):
    img = Image.open('white.png')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf",20)
    draw.text((0,0),text,(0,0,0),font = font)
    img.save("Text.png")
    await ctx.send(file = discord.File("text.png"))

@bot.command()
async def calR(ctx,a:int,b:int):
    width = a
    height = b
    cal = width * height
    await ctx.send('สูตร:')
    await ctx.send('กว้าง * ยาว = พื้นที่รูปสี่เหลื่ยม')
    await ctx.send(f'{width}(กว้าง) * {height}(ยาว) = (การหาพื้นที่รูปสี่เหลื่ยม){cal}')
@bot.command()
async def calT(ctx,a:int,b:int):
    side = a
    height = b
    cal =  side * height / 2
    await ctx.send(f'1/2 * {side} * {height} = {cal}')
@bot.command()
async def calP(ctx,a:int,b:int):
    base = a
    height = b
    cal = base * height
    await ctx.send(f'{base} * {height} = {cal}')

@bot.command()
async def clear(ctx, amount=1000):
	await ctx.channel.purge(limit=amount)

@bot.command()
async def mrp(ctx):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    inner_movietags = soup.select('td.titleColumn a')
    titles = [tag.text for tag in inner_movietags]
    n_movies = len(titles)
    idx = random.randrange(0,n_movies)
    rec = (f'หนังน่าดู {titles[idx]} บอกเลยว่าสนุก')
    em = discord.Embed(title = f"หนังที่ดีสำหรับ {ctx.author.name}",color = discord.Color.green())
    em.add_field(name = "ห นั ง คุ ณ ภ า พ",value= rec)
    em.set_thumbnail(url = f"https://image.freepik.com/free-vector/isometric-cinema-icon-set_1284-18691.jpg")
    em.set_footer(text = "ขอให้สนุกน้าาาาา",icon_url = "https://image.similarpng.com/very-thumbnail/2020/06/Icon-like-button-transparent-PNG.png")
    await ctx.send(embed=em)        
# @bot.command()
# @commands.has_any_role('!!OVB!!#6670', 'ผู้บัญชาการขอทานแห่งชาติ', 492212595072434186)
# async def cool(ctx):
#     await ctx.send('You are cool indeed')

@bot.command()
async def wait(ctx):
    await ctx.send('wait what')
    await asyncio.sleep(5)
    await ctx.send('wait what')
    
@bot.command()
async def emoji(ctx,*,text):
    emoji = []
    for i in text.lower():
        if i.isdecimal():
            num2emo = {1: ':one:', 2: ':two:', 3: ':three:', 4: ':four:', 5: ':five:', 6: ':six:', 7: ':seven:', 8: ':eight:', 9: ':nine:', 10: ':keycap_ten:'}
            emoji.append(f'{num2emo[int(i)]}')
        elif i.isalpha():
            emoji.append(f':regional_indicator_' + i + ':')
        elif i.isspace():
            emoji.append(f':heavy_minus_sign:')
        elif i != i.isalpha() and i != i.isdecimal() and i != i.isspace():
            await ctx.send('กูไม่มีอีโมจิ ไอเด็กเหี้ยนี้')
            return emoji
        else:
            await ctx.send('อย่าแม้แต่จะขึ้น')
            return emoji
        
    await ctx.send(''.join(emoji))

@bot.command()
async def calC(ctx,*,text):
    r = float(text) 
    c = 3.14159265358979323846264338327950288419716939937510582097494459230781650628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852 * r**2
    await ctx.send(f'พื้นที่วงกลม:\t{c}')

@bot.command()
async def Backpack(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()
    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]
    em = discord.Embed(title = f"{ctx.author.name}'s balance",color = discord.Color.green())
    em.add_field(name = "BOBCOIN balance",value= wallet_amt)
    em.add_field(name = "BOB Bank balance",value= bank_amt)
    await ctx.send(embed=em)

@bot.command()
async def TestJson(ctx):
    await open_account(ctx.author)
    users = await get_bank_data()
    user = ctx.author
    earning = random.randrange(101)
    await ctx.send(f"On my way son : God gave you {earning} coins!!")

    users[str(user.id)]["wallet"] += earning

    with open("mainbank.json","w") as f:
        json.dump(users,f)

@bot.command()
@commands.cooldown(1, 120, commands.BucketType.user)
async def lottery(ctx,text= None,amount=None):

    if text == None:
        await ctx.send("ใส่เลขด้วยสิเฮ้ย(ตัวเลข 5 หลักพอ)")
        return
    if text.isalpha():
        await ctx.send("ใส่ตัวเลขโว้ยยย(ตัวเลข 5 หลักพอ)")
        return
    bot = random.randrange(10000,99999)

    await ctx.send(f"เลขที่ออก {bot}")
    ans = float(text)
    if ans == bot:
        await ctx.send("สลุต่านชั่วข้ามคืน")
        await update_bank(ctx.author,100*amount)
    else:
        await ctx.send("ลางไม่ดีอีกแล้ววว")


@bot.event
async def on_message(msg):
    if "$reaction" in msg.content: 
        await msg.add_reaction("<:Discord:895553740793339986>")
        
    await bot.process_commands(msg) 
   
@bot.command()
async def QM(ctx):
    await open_account(ctx.author)

    member = ctx.author
    ran3 = random.randint(200,800)
    ran4 = random.randint(10000,99999)

    question = "%d + %d" % (ran3,ran4)
    answer = ran3 + ran4

    while True:
        await ctx.send(f"คำถามคือ {question}")
        print (answer)
        message = await bot.wait_for('message',check=lambda message: message.author == member)
        if message.content == str(answer)in message.content:
            await ctx.send("แกก็เก่งเหมือนกันนี้")
            await update_bank(ctx.author,500)
            return 
        
        else:
            await ctx.send("อ่อนหัด พยายามแค่ไหนก็ยังอ่อนหัด")
            await ctx.send("แต่ไม่เป็นไรรางวัลปลอบใจ 10 บาท")
            await update_bank(ctx.author,10)
            return 


@bot.command()
@commands.cooldown(1, 10, commands.BucketType.user)
async def slot(ctx,amount = None):
    datetime.now() + timedelta(seconds=10)
    await open_account(ctx.author)

    if amount == None:
        await ctx.send("ใส่เงินที่พนันด้วยสิเฮ้ย!")
        return
    bal = await update_bank(ctx.author)
    amount = int(amount)
    if amount > bal[0]:
        await ctx.send("เงินไม่พอ # จ น")
        return
    if amount < 0:
        await ctx.send("มึงหลอนป่าวเนี้ย มึงจะพนันเงินแต่ใส่ตัวเลขติดลบ คิดสิ คิด")
        return
    if amount == 0:
        await ctx.send("ใส่เลข 0 ทำเพื่อ?????")
        return
    if amount == float:
        await ctx.send("มึงอย่าแม้แต่จะคิด")
        return
    final = []
    for i in range(3):
        a = random.choice(["🍎","🍊","🍐"])
        final.append(a)
    
    message = await ctx.send("Slot Begin!")
    await asyncio.sleep(1)
    x = 0
    while x < 5:
        await message.edit(content = random.choice(["🍎🍊🍐","🍊🍐🍎","🍐🍎🍊"]))
        await asyncio.sleep(0.2)
        x += 1
    await message.edit(content = final)
    if final[0] == final[1] or final[0] == final[2] or final[2] == final[1]:
        await update_bank(ctx.author,5*amount)
        await ctx.send("ไอหมอนี้มันมาวะ")
    else:
        await update_bank(ctx.author,-20*amount)
        await ctx.send("ร ะ วั ง จ น น ะ")
@bot.command()
async def withdraw(ctx,amount = None):
    await open_account(ctx.author)

    if amount == None:
        await ctx.send("ใส่เงินที่ฝากด้วยสิเฮ้ย!")
        return
    bal = await update_bank(ctx.author)
    amount = int(amount)
    if amount > bal[1]:
        await ctx.send("เงินไม่พอ # จ น ")
        return
    if amount < 0:
        await ctx.send("มึงหลอนป่าวเนี้ย มึงจะฝากเงินแต่ใส่ตัวเลขติดลบ คิดสิ คิด!")
        return
    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,-1*amount,"bank")

    await ctx.send(f"คุณถอนเงินจำนวน {amount} เหรียญ!")
@bot.command()
async def leaderboard(ctx,x = 3):
    users = await get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        print("TEST")
        name = int(user)
        total_amount = users[user]["wallet"] + users[user]["bank"]
        leader_board[total_amount] = name
        total.append(total_amount)
    total = sorted(total,reverse=True)

    em = discord.Embed(title = f"Top {x} จตุรเทพแห่งความมั่นคั่ง",description = "จตุรเทพแห่งความมั่นคั่ง",color = discord.Color.purple())
    index = 1
    for amt in total:
        print("TEST1")
        id_ = leader_board[amt]
    
        user = await bot.fetch_user(id_)
        
        print("TEST2")
        em.add_field(name = f"{index}. {user}",value = f"{amt}",inline = False)
        if index == x:
            break
        else:
            index += 1
    await ctx.send(embed = em)
@bot.command()
async def deposit(ctx,amount = None):
    await open_account(ctx.author)

    if amount == None:
        await ctx.send("ใส่เงินที่ถอนด้วยสิเฮ้ย!")
        return
    bal = await update_bank(ctx.author)
    amount = int(amount)
    if amount > bal[0]:
        await ctx.send("เงินไม่พอ # จ น ")
        return
    if amount < 0:
        await ctx.send("มึงหลอนป่าวเนี้ย มึงจะถอนเงินแต่ใส่ตัวเลขติดลบ คิดสิ คิด!")
        return
    await update_bank(ctx.author,-1*amount)
    await update_bank(ctx.author,amount,"bank")

    await ctx.send(f"คุณฝากเงินจำนวน{amount} เหรียญ!")

async def open_account(user):
    users = await get_bank_data()
    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 0
        users[str(user.id)]["bank"] = 0

    with open("mainbank.json","w") as f:
        json.dump(users,f)
    return True

async def get_bank_data():
    with open("mainbank.json","r") as f:
        users = json.load(f)
    return users

async def update_bank(user,change = 0,mode = "wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] +=change

    with open("mainbank.json","w") as f:
        json.dump(users,f)
    bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
    return bal

@bot.command()
async def invite(ctx):
    em = discord.Embed(title = f"BOB's BOBCOIN",color = discord.Color.purple())
    em.add_field(name = "BOBCOIN",value="https://discord.com/api/oauth2/authorize?client_id=880963590289498142&permissions=8&scope=bot")
    em.set_thumbnail(url = "https://cdn.discordapp.com/attachments/865170212822319114/894807330313621535/Discord.png")
    em.set_footer(text = "บ อ ท แ ห่ ง ช น ชั้ น",icon_url = "https://cdn.discordapp.com/attachments/865170212822319114/894807330313621535/Discord.png")
    await ctx.send(embed=em)

@bot.command()
async def ER(ctx):
  message = await ctx.send("hello")
  await asyncio.sleep(1)
  await message.edit(content="newcontent")

@bot.command()
async def command(ctx):

    em = discord.Embed(title = "Info",
        description = "prefix $\nคำสั่งตามด้วย[TC] = Test Command\nคำสั่งตามด้วย[FT] = Feature Command",
        color = discord.Color.purple())
    em.set_author(name = "BOBCOIN COMMANDS",icon_url = "https://cdn.discordapp.com/attachments/865170212822319114/894807330313621535/Discord.png")
    em.add_field(name = "DTC ตามด้วยข้อความ [TC]",value = "Test image(TYPE TEXT) manipulation",inline = False)
    em.add_field(name = "stonk ตามด้วย@user [TC]",value = "Test image(TYPE USER) manipulation",inline = False)
    em.add_field(name = "ER [TC]",value = "Test Message Edit",inline = False)
    em.add_field(name = "TestJson [TC]",value = "Test Money Given System",inline = False)
    em.add_field(name = "wait [TC]",value = "Test Asyncio",inline = False)
    em.add_field(name = "QM [FT]",value = "Quick Math Feature",inline = False)
    em.add_field(name = "calP ตามด้วย ฐาน(ตัวเลข) และ สูง(ตัวเลข) [FT]",value = "Calculator Paralleogram Feature",inline = False)
    em.add_field(name = "calR ตามด้วย กว้าง(ตัวเลข) และ ยาว(ตัวเลข) [FT]",value = "Calculator Rectangle Feature",inline = False)
    em.add_field(name = "calT ตามด้วย ผลบวกด้านคู่ขนาน(ตัวเลข) และ สูง(ตัวเลข) [FT]",value = "Calculator Trapezoid Feature",inline = False)
    em.add_field(name = "calC ตามด้วย รัศมี(ตัวเลข) [FT]",value = "Calculator Circle Feature",inline = False)
    em.add_field(name = "clear [FT]",value = "Delete Message Feature",inline = False)
    em.add_field(name = "invite [FT]",value = "Invite BOB's BOBCOIN Feature",inline = False)
    em.add_field(name = "deposit [FT]",value = "Deposit BOBCOIN Feature",inline = False)
    em.add_field(name = "withdraw [FT]",value = "Withdraw From BOB Bank Feature",inline = False)
    em.add_field(name = "Backpack [FT]",value = "Check Your Backpack Feature",inline = False)
    em.add_field(name = "lottery ตามด้วยตัวเลข 5 หลัก [FT]",value = "Lottery Feature",inline = False)
    em.add_field(name = "slot ตามด้วยเงินพนัน [FT]",value = "Slot Feature",inline = False)
    em.add_field(name = "leaderboard [FT]",value = "Leader board Feature",inline = False)
    #em.add_field(name = "coinflip [FT]",value = "Coin Flip Feature",inline = False)
    em.add_field(name = "emoji ตามด้วยข้อความ(ENG ONLY) [FT]",value = "Convert Text To Emoji Feature",inline = False)
    em.add_field(name = "mrp [FT]",value = "Recommend Moive Feature",inline = False)
    
    em.set_thumbnail(url = "https://media2.giphy.com/media/Fo5y4K3GD3RYijvsCS/200.gif")
    em.set_footer(text = "| บ อ ท แ ห่ ง ช น ชั้ น น |",icon_url = "https://cdn.discordapp.com/attachments/865170212822319114/894807330313621535/Discord.png")
    await ctx.send(embed = em)


bot.run('Token')
