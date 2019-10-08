## NEW VERSION - 10/Oct/2019

**To manage the bot, go to your browser of preference after running joker.py and type http://localhost:5555**

# JokerCord

Check future plans here! https://github.com/joker-ware/JokerCord/wiki

Welcome to JokerCord Pokécord SelfBot. This bot has been made by JokerWare and it is aimed for cheating the PokéCord Discord bot. Please be aware I am not responsible for any bans or problems caused by the usage of this bot. Use at your own risk.

**ATTENTION. Until further notice, the bot only catches Pokemons in the same server of which "spam_channel" pertains. This is being worked on and will be fixed in a future update.**

This bot is under heavy development. I am aware not all names are correct and I'm working to find a solution as soon as possible. This requires A LOT of research from my part and I'm currently studying a degree so my time is limited, please take that into account. Lastly, let me thank you for stopping by and giving my project a shot. Remember that contributions are always appreciated. <3


## Installation

Just make sure to have installed the last Python version. You can download it here: 

[Download the latest Python version](https://www.python.org/downloads/)

A brief list of the required libraries can be seen below.


## Beginner Guide
If you wanna use this bot, just click on the green button that says "Clone or Download" and select Download to Zip. Extract the folder anywhere you like.


If you have never used Python, this will guide you through each step in order to make this bot work.

First of all, identify your Operating System (Windows, GNU/Linux, MacOS...)

## For Linux
Open a terminal session and run apt update:
```bash
sudo apt-get update
```
Install Python3 and Pip:
```bash
sudo apt-get install python3 && sudo apt-get install python3-pip
```
To install the required libraries, simply run pip as follows:
```bash
pip3 install discord.py dhash imagehash requests python-resize-image pillow flask
```
Lastly, to run JokerCord navigate to the downloaded folder:
```bash
cd /path/to/the/folder
```
Please make sure the path is the same as joker.py or else the bot will probably not work.
Then run it with python3:
```bash
python3 joker.py
```
## For Windows
Firstly make sure to download Python from the link provided above. When installing check the box that says *add Python to Path*.
After it finishes installing, you can open the Windows console by pressing <kbd>⌘R</kbd> and typing
```bash
cmd
```
In the search box. After the console opens, you can install each library by typing:
```bash
pip3 install discord.py dhash imagehash requests python-resize-image pillow flask
```
**NOTE**
This will not work if you didn't add Python to the PATH as referenced before.
After installing all the dependencies, just close the terminal and open your File Manager. Go to the Downloaded folder and double click joker.py. You're done!

## Usage

After you start joker.py, navigate to http://localhost:5555 to manage the bot, and go to Preferences to add your token. 

**Getting your token**

To get your discord token: [Tutorial](https://discordhelp.net/discord-token)

To get a channel ID, first enable discord developer mode by accesing Settings>Appearance>Enable developer mode ,and then right click on any channel and select ID.

## Contributing
Any bugs you find please consider sending them. Do notice this bot is in a very early beta stage so not all names will be correct.


## Required libraries
- [Discord.py](https://pypi.org/project/discord.py/)
- [dHash](https://pypi.org/project/dhash/)
- [ImageHash](https://pypi.org/project/ImageHash/)
- [Requests](https://pypi.org/project/requests/)
- [Resizeimage](https://pypi.org/project/python-resize-image/)
- [PIL](https://pypi.org/project/Pillow/)
