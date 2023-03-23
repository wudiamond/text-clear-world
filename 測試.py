import discord
import time
intents = discord.Intents.default()
client = discord.Client(intents=intents)
@client.event
async def on_message(message):
    if message.content == '!load':
       await message.delete()
       loading_message = await message.channel.send('載入中...<a:dm_loading:1071960925290111058>')
       time.sleep(1)
       await message.channel.send(f'!edit_message {loading_message.id}')
    if message.content.startswith('!edit_message'):
        # Split the message content into parts
        parts = message.content.split(' ')
        await message.delete()
        # Check if there are enough parts
        if len(parts) < 2:

            await message.channel.send("Error: Not enough arguments")
            return
        
        # Extract the message ID and new content
        message_id = int(parts[1])
        new_content = ' '.join(parts[2:])
        

        # Fetch the message and edit its content
        message_to_edit = await message.channel.fetch_message(message_id)
        for i in range(3):
            await message_to_edit.edit("Iteration: ", i+1)

            await message_to_edit.edit(content=f"**[** ***{message.channel}*** **]**已經載入完畢<a:dm_ok:1071961783381794896> ")
client.run('MTA4MTQ3Mzk5Njc0ODQ4ODcxNQ.GMs-bV.JIQEDp9ILfkQ0dvoB8fO4AgLl5liC3jxeuVOIw')