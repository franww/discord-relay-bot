import discord
from discord.ext import commands
from keep_alive import keep_alive
import os


intents = discord.Intents.default()
intents.message_content = True 
intents.guilds = True


bot = commands.Bot(command_prefix="!", intents=intents)

CANAL_ORIGEM_ID = 1292499842643267594
CANAL_DESTINO_ID = 1292490095034634354

keep_alive()

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.channel.id == CANAL_ORIGEM_ID:
        canal_destino = bot.get_channel(CANAL_DESTINO_ID)

        if canal_destino is not None:
            if message.content or message.embeds:
                
                if message.content:
                    await canal_destino.send(message.content)
                if message.embeds:
                    for embed in message.embeds:
                        await canal_destino.send(embed=embed)
            else:
                print("Mensagem vazia, nada a enviar.")
        else:
            print(f'Canal destino {CANAL_DESTINO_ID} não encontrado.')

bot.run('token')
