import discord
import random
import os
import requests
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')  


@bot.command()
async def meme(ctx):
    img_nome = random.choice(os.listdir('images'))
    with open(f'images/{img_nome}', 'rb') as f:
        #Vamos armazenar o arquivo convertido da biblioteca do Discord nesta variável!
        picture = discord.File(f)
    # Podemos então enviar esse arquivo como um parâmetro
    await ctx.send(file=picture)
    

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Uma vez que chamamos o comando duck, o programa chama a função get_duck_image_url '''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
    
   
def get_fox_image_url():   
    url = ''
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('fox')
async def fox(ctx):
    '''Uma vez que chamamos o comando fox, o programa chama a função get_fox_image_url '''
    image_url = get_fox_image_url()
    await ctx.send(image_url)

bot.run('')
