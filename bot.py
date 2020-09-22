import discord
from discord.ext import commands

client = commands.Bot(command_prefix="!")



rules = [
    ":one: No Racism of any form",
    ":two: Stay on topic",
    ":three: Maintain Peace",
    ":four: Do not Spam",
    ":five: Respect Everyone"
]

filtered_words = ['cats','birds','dogs','bad'] #These are some of the words that won't be allowed in the server like any swear words/any abusive words.
# Bot would delete the message instantly if it finds any sentence that contains these words

@client.event  #client decorator
async def on_ready():
    print('Bot is ready')

@client.event #client decorator for an event that would involve a person trying to send any kind of abusive message
async def on_message(msg):
    for word in filtered_words:
        if word in msg.content:
            await msg.delete()
    await client.process_commands(msg)

@client.command() #Greets the user
async def hello(ctx):
    await ctx.send("Hey !")

@client.command() #Displays the rule specified by the user
async def rule(ctx,*,number):
    await ctx.send(rules[int(number)-1])

@client.command() #displays all the rules of the server
async def showrules(ctx):
    await ctx.send(str(rules[:]))

@client.command() #Admin Rights of deleting messages
@commands.has_permissions(manage_messages = True) #This ensures that only the user having such privelage of managing messages then only the command will execute
async def clear(ctx,amount=3): #If nothing is passed in then it will delete latest 2 messages
    await ctx.channel.purge(limit = amount)

@client.command() #Admin Rights of Removing any member.
@commands.has_permissions(kick_members = True) #This ensures that only the user having such privelage of removing any member then only the command will execute
async def kick(ctx,member : discord.Member): #Takes the member as the member object(will have to enter the discord id)
    await member.send('You have been removed from the server') #This will DM the kicked person the specified message
    await member.kick()




@client.command()
async def emoji(ctx):
    await ctx.send("🔥")
    await ctx.send("😊")
    await ctx.send("👍")
    await ctx.send("😂")
    await ctx.send("🤣")

client.run("NzQzNzg2NzYxMjU5NTgxNTQw.XzZvZg.4uo_UXSTmErhoeSXsNyjZLlCw7Q") #Passing the unique token To run the bot


