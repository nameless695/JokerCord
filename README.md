# JokerCord

Welcome to JokerCord Pokécord SelfBot. This bot has been made by JokerWare and it is aimed for cheating the PokéCord Discord bot. Please be aware I am not responsible for any bans or problems caused by the usage of this bot. Use at your own risk.

## Installation

Just make sure to have installed the last Python version. You can download it here: 

[Download the latest Python version](https://www.python.org/downloads/)

A brief list of the required libraries can be seen below.

## Useful commands
```bash
_list_state True/False
```
Enables or disables custom catch list.
```bash
_add Pokemon
```
Adds specified Pokemon to the catch list.
```bash
_add_bulk Pokemon1,Pokemon2,Pokemon3,Pokemon4...
```
Adds every Pokemon in the list. Please separate each Pokemon with a comma ","

## Beginner Guide
If you have never used Python, this will guide you through each step in order to make this bot work.

First of all, identify your Operating System (Windows, GNU/Linux, MacOS...)
**For Linux**
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
pip3 install discord.py && pip3 install dhash && pip3 install imagehash && pip3 install requests && pip3 install python-resize-image && pip3 install PIL
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
## Usage

Edit the file preferences.json file to add your token and enable the auto-spam function in case you wanted it. Auto spam comes disabled by default.

To run the bot you need to open your System terminal and run

```bash
python3 /Path/to/the/folder/joker.py
```
Please run it inside the Bot folder. 
## Contributing
Any bugs you find please consider sending them. Do notice this bot is in a very early beta stage so not all names will be correct.


## Required libraries
- [Discord.py](https://pypi.org/project/discord.py/)
- [dHash](https://pypi.org/project/dhash/)
- [ImageHash](https://pypi.org/project/ImageHash/)
- [Requests](https://pypi.org/project/requests/)
- [Resizeimage](https://pypi.org/project/python-resize-image/)
- [PIL](https://pypi.org/project/Pillow/)
