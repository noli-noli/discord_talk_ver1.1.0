import discord
import voice
import os
import random
import time
import subprocess
from collections import defaultdict, deque
import asyncio
import re


queue_dict = defaultdict(deque)
intents = discord.Intents.all()
intents.typing = True
client = discord.Client(intents=intents)
debug_mode = False
Channel = "blank"

def enqueue(voice_client, guild, source):
    queue = queue_dict[guild.id]
    queue.append(source)
    if not voice_client.is_playing():
        play(voice_client, queue)

def play(voice_client, queue):
    if not queue or voice_client.is_playing():
        return
    source = queue.popleft()
    voice_client.play(source, after=lambda e:play(voice_client, queue))

async def text(text,message):
    global debug_mode
    if debug_mode == True:
        await message.channel.send("```cs\n" + "# " + text +"\n```")
    else:
        await message.channel.send(text)

@client.event
async def on_ready():
    print("start-up success")

@client.event
async def on_message(message):
    global Channel
    if message.author.bot:
        return
    
    if message.content == "rui help":
        await text("    --command list--   ",message)
        await text("rui join <== ボイスチャンネルにマージ",message)
        await text("rui exit <== ボイスチャンネルからパージ",message)
        await text("rui debug_mode <== デバッグモード [off or on]",message)
        await text("rui config <== ボイスコンフィグレーション",message)
        await text("rui -v <== バージョン表示",message)

    elif message.content == "rui join":
        if message.author.voice == None:
            await text("貴殿のボイスチャンネルに対するアクセスを希望",message)
            return
        Channel = message.channel
        await message.author.voice.channel.connect()
        await text("ボイスチャンネルにマージ",message)
        tmp = random.randrange(0,10)
        print(tmp)
        if (tmp == 0 or tmp == 1):
            await text("幼女に踏まれたい",message)
        elif(tmp == 2):
            await text("男の子は乳首だけは女の子なんですよ。",message)
        elif(tmp == 3):
            await text("もっちゃん！左乳首に改名しようよ！",message)
    elif message.content == "rui exit":
        if message.guild.voice_client == None:
            await text("現在ボイスチャンネルにアクセスしておらず",message)
            return
        await message.guild.voice_client.disconnect()
        await text("ボイスチャンネルからパージ",message)
    #実験用
    elif message.content == "rui test":
        await text("hello",message)

    elif message.content == "rui debug_mode":
        global debug_mode
        if debug_mode != True:
            debug_mode = True
            await text("debug_mode on",message)
        else:
            debug_mode = False
            await text("debug_mode off",message)

    elif message.content == "rui config":
        pass
    
    elif message.content == "rui -v":
        await text(str(subprocess.run("vmstat",capture_output=True,text=True,shell=True)),message)
        await text(str(subprocess.run("uname -a",capture_output=True,text=True,shell=True)),message)
        await text(str(subprocess.run("python3 -V",capture_output=True,text=True,shell=True)),message)
        await text(str(subprocess.run("pip list | grep discord",capture_output=True,text=True,shell=True)),message)

    else:
        cheak = message.channel
        print(cheak)
        if Channel != cheak:
            return
        if message.guild.voice_client:
            print(message.content)
            if re.search("<:emoji_3:977475896892076112>",message.content) != None:
                enqueue(message.guild.voice_client,message.guild,discord.FFmpegPCMAudio("kobuside.wav"))
            elif re.search("<:emoji_1:1026651103309340784>",message.content) != None:
                enqueue(message.guild.voice_client,message.guild,discord.FFmpegPCMAudio("kobuside.wav"))
            elif re.search("<:emoji_11:1019209102150357082>",message.content) != None:
                enqueue(message.guild.voice_client,message.guild,discord.FFmpegPCMAudio("kibokura.wav"))
            elif re.search("<:emoji_13:1050841436758745168>",message.content) != None:
                enqueue(message.guild.voice_client,message.guild,discord.FFmpegPCMAudio("saki.wav"))
            elif re.search("<:emoji_14:1050842395190763590>",message.content) != None:
                enqueue(message.guild.voice_client,message.guild,discord.FFmpegPCMAudio("saki.wav"))
            elif re.search("<:utan:1051049802810544178>",message.content) != None:
                enqueue(message.guild.voice_client,message.guild,discord.FFmpegPCMAudio("u-tan.wav"))
            else:
                voice.creat_voice(message.content)
                enqueue(message.guild.voice_client,message.guild,discord.FFmpegPCMAudio("output.wav"))
        else:
            pass

client.run("MTAyMDE4ODc3MzMwMjE2MTQxOA.G2Z9W0.2GczTxaw_U1j76padbUY4LJeglVpBRGUnYmYhY")