from library import *

#Define write to json
def write_json(wrtline, wrt):
    try:
        with open(path + "/preferences.json") as pr:
            jsdecoded = json.load(pr)
            jsdecoded[str(wrtline)] = str(wrt)
        with open(path + "/preferences.json", 'w') as jfil:
            json.dump(jsdecoded, jfil)
    except Exception as e: print(e)
#Path
path = os.path.dirname(os.path.abspath(sys.argv[0]))
#Presets
with open (path + "/preferences.json") as p:
    prefs = json.load(p)
#Start
if(prefs["local"] == "False"):
    correct_spam = 0
    correct_channel = 0
    correct_interval = 0
    print("Welcome to JokerCord Pokecord selfbot. The prefix is _ . You can enable auto spam in preferences.json. Please do notice this is in beta stage and we do no assure all pokemons are correct. If you see that the names are incorrect, you can head to preferences.json and change the hash type to phash or dhash. We are not responsible for any bans.")
    time.sleep(2)
    print("You will be prompted some details before continuing.")
    print("Please input your discord token. Don´t worry, it won't be shared with anyone.")
    token_raw = input("Insert your token: ")
    write_json("token", token_raw)
    time.sleep(1)
    while(correct_spam == 0):
        auto_spam_raw = input("Please choose whether to activate auto-spam (True/False): ")
        if(auto_spam_raw != "True" and auto_spam_raw != "False"):
            print("Please select True or False")
        else:
            write_json("auto_spam", auto_spam_raw)
            time.sleep(3)
            correct_spam = 1
    
    while(correct_channel == 0):
        auto_spam_channel_raw = input("Please type the desired channel id: (Type - if you dont want auto spam): ")
        if(auto_spam_channel_raw == "-"):
            correct_channel = 1
        elif(len(auto_spam_channel_raw) != 18 or auto_spam_channel_raw.isdigit() != 1):
            print("Please type a valid channel id")
        else:
            write_json("auto_spam_channel", auto_spam_channel_raw)
            correct_channel = 1
    while(correct_interval == 0):
        auto_spam_interval_raw = input("Please type the desired spam interval in seconds (Type - if you dont want auto spam, default is 5s): ")
        if(auto_spam_interval_raw == "-"):
            correct_interval = 1
        elif(auto_spam_interval_raw.isdigit() != 1):
            print("Please type a valid time interval.")
        else:
            write_json("auto_spam_interval", auto_spam_interval_raw)
            correct_interval = 1
    auto_spam_text = input("Lastly, please input the spam text: ")
    write_json("auto_spam_text", auto_spam_text)
    write_json("local", "True")
    print("Please restart the bot to continue.")
    sys.exit(0)
if(prefs["token"] == "INSERT YOUR TOKEN HERE. DONT REMOVE THE QUOTATION MARKS"):
    print("Please insert a valid token in preferences.json")
    sys.exit(0)
#Pref
client = commands.Bot(command_prefix='_')

#Defines
def getpHash(img):
    io = Image.open(img)
    hashp = imagehash.phash(io)
    return hashp
def getdHash(img):
    io = Image.open(img)
    hashd = imagehash.dhash(io)
    return hashd
##########

#Lists
with open (path + '/Lists/phash.json') as pd:
    pdata = json.load(pd)
with open (path + '/Lists/dhash.json') as dd:
    ddata = json.load(dd)
#End

#Ready
@client.event
async def on_ready():
    print("JokerCord is connected and running. Version : BETA 0.0.2")
    if(prefs["auto_spam"] == "True"):
        while(1):
            #try:
                channel = client.get_channel(int(prefs["auto_spam_channel"]))
                await channel.send(prefs["auto_spam_text"])
                await asyncio.sleep(int(prefs["auto_spam_interval"]))
            #except:
    
@client.event
async def on_message(message):
    ev = 1
    #Get the embed message
    try:
        embed = message.embeds[0]
    except IndexError:
        ev = 0
    #Check if message is from Pokecord Spawn
    if (message.author.id != client.user.id and ev == 1): #and "A wild" in message.content):
        
        try:
            url = embed.image.url
            try:
                    if 'discordapp' not in url:
                        return
            except TypeError:
                    return
            print(url)
            #Open image and save it to JPG
            openimg = open(path + '/Assets/pokemon.jpg','wb')
            openimg.write(requests.get(url).content)
            openimg.close()
            

                #Get hashes

            rphash = getpHash(path + '/Assets/pokemon.jpg')
            rdhash = getdHash(path + '/Assets/pokemon.jpg')

            #Compare hashes with the lists
            dummy = 100
            save_line = None
            if(prefs["hash_type"] == "phash"):

                for line in pdata:
                    compare_hex = int(str(rphash), 16)
                    compare_file = int(pdata[line], 16)
                    diff = dhash.get_num_bits_different(compare_hex,compare_file)
                    if(diff < dummy):
                        dummy = diff
                        save_line = line
                await message.channel.send("p!catch " + save_line)
            elif(prefs["hash_type"] == "dhash"):
                for line in ddata:
                    compare_hex = int(str(rdhash), 16)
                    compare_file = int(ddata[line], 16)
                    diff = dhash.get_num_bits_different(compare_hex,compare_file)
                    if(diff < dummy):
                        dummy = diff
                        save_line = line
                await message.channel.send("p!catch " + save_line)
            else:
                await message.channel.send("There has been an error with the config file. Please refer to preferences.json or contact the developer. Please make sure 'hash_type' is either phash or dhash.")
        except AttributeError:
            return
    await client.process_commands(message)

@client.command()
async def pref(message):
    await message.channel.send(prefs["hash_type"])

client.run(prefs["token"], bot=False)