import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True 
intents.guilds = True


bot = commands.Bot(command_prefix="!", intents=intents)

CANAL_ORIGEM_ID = first id
CANAL_DESTINO_ID = second id


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
