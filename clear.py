import discord
import asyncio

client = discord.Client()
token = 'you token'
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event


async def on_message(message):
    if message.channel.id == 頻道id:
        await message.add_reaction('<a:dm_101:1072339232867237898>')
        await asyncio.sleep(10)
        await message.delete()



client.run(token)
