#Actual Project
#Self Care Discord Bot "Zoomie"

import discord
from discord.ext import commands

client = discord.Client()

@client.event
async def on_message(message):
    message.content = message.content.lower()
    if message.author == client.user:
        return
    if message.content.startswith("hello"):
       
        if message.content.startswith("Hello"):
            await message.channel.send("Hello, My name is Zoomie.")   
    if str(message.author) == "ShayFlem#8584":
        await message.channel.send("Greetings " + str(message.author) + " !")
    else: 
        await message.channel.send("Hello, My name is Zoomie.")




#This deletes non image entries - text
#@client.event
#async def on_message(message):
   # if str(message.channel) == "general" and message.content != "":
     #   await message.channel.purge(limit=1)

client = commands.Bot(command_prefix="$")

#This does a list of arguments
@client.command()
async def checkin(ctx, *args):
    for arg in args:
        await ctx.send(arg)


List = ["Be Kind to Yourself","Zoomie Loves You =)", "Life Will Get Better","Make Sure You Eat Today"]
print("\nAffirmation List: ") 
print(List[0])  
print(List[1]) 
print(List[2])  
print(List[3]) 














client.run("NzY2OTExNzE2NTI4NDg4NDY4.X4qQMQ._tVC7A7jBTLFtH45LEeTBscMDcQ")
