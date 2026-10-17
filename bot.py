import os
import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

token = os.getenv('TOKEN')
if token:
    client.run(token)
else:
    print("Erro: A variável de ambiente TOKEN não foi encontrada!")
