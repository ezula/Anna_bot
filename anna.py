import discord
from discord.ext.commands import Bot
from discord.ext import commands
from quiz import Trivia
import random
from secrets import BOT_TOKEN

Client = discord.Client()
anna_Bot = commands.Bot(command_prefix="!")

""" This is a discord Bot named Anna """

@anna_Bot.event
async def on_ready():
    print("Logged in")
    print("Name: {}".format(anna_Bot.user.name))
    print("ID: {}".format(anna_Bot.user.id))
    print(discord.__version__)


@anna_Bot.command(pass_context = True)
async def hello(ctx):
    return await anna_Bot.say("Hello {}! My friend!".format(ctx.message.author.name))

@anna_Bot.command(pass_context = True)
async def commands(ctx):
    return await anna_Bot.say("Here is some commands you can use: \n\n!hello \n\n!trivia")

@anna_Bot.command(pass_context = True)
async def trivia(*args):
    return await anna_Bot.say("trivia is not ready yet!")

@anna_Bot.command(pass_context = True)
async def rekt(ctx):
    return await anna_Bot.say("They don't deserve like this, {}! Don't deserve for rekt! - Pashabiceps".format(ctx.message.author.name))

@anna_Bot.event
async def on_member_join(member):
    server = member.server
    msg = "Welcome {0.mention} to {1.name}!"
    await anna_Bot.send_message(server, msg.format(member, server))
            

anna_Bot.run(BOT_TOKEN())
