import discord
from discord.ext.commands import Bot
import asyncio
import json
import requests
import time
from discord.ext import commands
from PIL import Image
import sys, os
import random
import hashlib
from threading import Thread

legendaries = ['arceus', 'articuno', 'azelf', 'celebi', 'cobalion', 'cosmoem', 'cosmog', 'cresselia',
            'darkrai', 'deoxys', 'dialga', 'diancie', 'Entei', 'genesect', 'giratina', 'groudon',
            'heatran', 'ho-Oh', 'hoopa', 'jirachi', 'Keldeo', 'kyogre', 'kyurem', 'landorus',
            'latias', 'latios', 'lugia', 'lunala', 'Magearna', 'manaphy', 'marshadow', 'meloetta',
            'mesprit', 'mew', 'mewtwo', 'moltres', 'Necrozma', 'palkia', 'phione', 'raikou',
            'rayquaza', 'regice', 'regigigas', 'regirock', 'registeel', 'reshiram', 'shaymin', 'silvally',
            'solgaleo', 'suicune', 'tapu bulu', 'tapu fini', 'tapu koko', 'tapu lele', 'terrakion', 'thundurus',
            'tornadus', 'type: null', 'uxie', 'victini', 'virizion', 'volcanion', 'xerneas', 'yveltal', 'naganadel']

#Define write to json
def file_read(folder, fname):
    caught = open(path + "/" + folder + "/" + fname, "r")
    lines = caught.readlines()
    caught.close()
    return lines
def clear_file(folder, fname):
    open(path + "/" + folder + "/" + fname, 'w').close()
def file_append(folder, fname, append):
    p = (path + "/" + folder + "/" + fname)
    f = open(p, "a")
    f.write(append + " ")
    f.close()
def add_pokemon(name):
    try:
        with open(path + "/User/customs.json") as cs:
            jsdecoded = json.load(cs)
            jsdecoded[str(name)] = ""
            cs.close()
        with open(path + "/User/customs.json", 'w') as jfil:
            json.dump(jsdecoded, jfil)
            jfil.close()
    except Exception as e: print(e)
def write_json(wrtline, wrt):
    try:
        with open(path + "/preferences.json") as pr:
            jsdecoded = json.load(pr)
            jsdecoded[str(wrtline)] = str(wrt)
            pr.close()
        with open(path + "/preferences.json", 'w') as jfil:
            json.dump(jsdecoded, jfil)
            jfil.close()
    except Exception as e: print(e)
#Path
path = os.path.dirname(os.path.abspath(sys.argv[0])).replace("/WebServer", "")
#Presets
with open (path + "/preferences.json") as p:
    prefs = json.load(p)
    p.close()
with open (path + "/User/guilds.json") as g:
    guild_list = json.load(g)
    g.close()
with open (path + "/User/channels.json") as ch:
    channel_list = json.load(ch)
    ch.close()
with open (path + "/User/customs.json") as cs:
            custom_list = json.load(cs)
            cs.close()
#Start
#Pref
client = commands.Bot(command_prefix='_')

#Defines
async def spamThread(channelInstance,delay):
    while(True):
        await channelInstance.send("Random text")
        await asyncio.sleep(int(delay))
def gethash(img):
    with open (img, "rb") as h:
        md = hashlib.md5(h.read()).hexdigest()
        h.close()
    return md
##########

#Lists
with open (path + '/Lists/hashes.json') as h:
    hashdata = json.load(h)
    h.close()

#End

#Ready
@client.event
async def on_ready():
    user_guilds = client.guilds
    for guild in user_guilds:
        try:
            if(guild_list[str(guild.id)] and guild_list[str(guild.id)][3]):
                guild_list[str(guild.id)] = [guild_list[str(guild.id)][0], guild.name, guild.icon, guild_list[str(guild.id)][3]]
                        
        except:
            guild_list[str(guild.id)] = ["False", guild.name, guild.icon, "2"]
        finally:
            for channel in guild.text_channels:
                try:
                    if(channel_list[str(channel.id)][1] == "True" or channel_list[str(channel.id)][1] == "False"):
                        pass
                except:
                    channel_list[channel.id] = [channel.name+"@"+guild.name, "False", "5"]
            with open (path + "/User/channels.json", 'w') as clr_channels:
                clr_channels.write("{}")
                clr_channels.close()

            with open(path + "/User/channels.json", 'w') as jfil:
                json.dump(channel_list, jfil)
                jfil.close()
    try:
        with open (path + "/User/guilds.json", 'w') as clr_guilds:
            clr_guilds.write("{}")
            clr_guilds.close()
        with open(path + "/User/guilds.json", 'w') as jfil:
            json.dump(guild_list, jfil)
            jfil.close()
    except Exception as e: print(e)
    for channel in channel_list:
        if channel_list[channel][1] == "True":
            spchannel = client.get_channel(int(channel))
            client.loop.create_task(spamThread(spchannel,channel_list[channel][2]))
    print("JokerCord is connected and running. Version : Multi-1.0.0")

    
@client.event
async def on_message(message):
    ev = 1
    #Get the embed message
    try:
        embed = message.embeds[0]
    except IndexError:
        ev = 0
    #Check if message is from Pokecord Spawn
    if (message.author.id != client.user.id and ev == 1 and (guild_list[str(message.guild.id)][0] == "True")): #and "A wild" in message.content):
        
        try:
            url = embed.image.url
            try:
                    if 'discordapp' not in url:
                        return
            except TypeError:
                    return
            #print(url)
            #Open image and save it to JPG
            openimg = open(path + '/Assets/pokemon.jpg','wb')
            openimg.write(requests.get(url).content)
            openimg.close()
            
            

                #Get hashes

            mdhash = gethash(path + '/Assets/pokemon.jpg')
            #Compare hashes with the lists
            save_line = None
            
            for i in hashdata:
                
                if (hashdata[i] == mdhash):
                    save_line = i
                    break
            if(save_line in legendaries):
                await asyncio.sleep(3)
            else:
                await asyncio.sleep(int(guild_list[str(message.guild.id)][3]))
            if(prefs["custom_list"] == "True"):
                if(save_line in custom_list):
                    await message.channel.send("p!catch " + save_line.lower())
                    if (save_line not in file_read("User", "caught.txt")):
                        file_append("User","caught.txt",save_line)
            else:
                await message.channel.send("p!catch " + save_line.lower())
                if (save_line not in file_read("User", "caught.txt")):
                    file_append("User","caught.txt",save_line)      
                    
                else:
                    return
        except AttributeError:
            return
    


 
