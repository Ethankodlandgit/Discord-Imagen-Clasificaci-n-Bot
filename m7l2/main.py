import discord 
from discord.ext import commands
from model import get_class 
import requests 

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/',intents=intents)

@bot.event 
async def on_ready():
    print(f'Hola estamos logiado como {bot.user}')

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attaccments in ctx.message.attachments:
            file_name = attaccments.filename
            file_url= attaccments.url
            await attaccments.save(f"./{attaccments.filename}")
            await ctx.send(get_class(model_path="./keras_model.h5",labels_path="labels.txt",image_paht=f"./{attaccments.filename}"))
    else:
        await ctx.send("ohhh, No has subido ninguna foto")
        
bot.run('MTMxNjkyMTg3NzcxNzA1NzU4Nw.GiHzym.W9-yfIALzIaJnRCcdxntfOCoL9XMjJFXi2iW1o')


