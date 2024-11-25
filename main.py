#timeout login is sillypass btw :333

import discord
import io
import sys

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!echo '):
        await message.channel.send(message.content[6:])

    if message.content.startswith('!code '):
        with open("main.py", 'w') as overwrite:
            overwrite.write("no peeking! :3")

        output = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = output

        exec(message.content[6:])

        sys.stdout = old_stdout
        result = output.getvalue()
        output.close()
        
        chunk_len=1994
        if len(result) > chunk_len:
            for i in range(0, len(result), chunk_len):
                await message.channel.send('```'+result[i:chunk_len+i]+'```')
        else:
            await message.channel.send('```'+result+'```')


client.run("token goes here")
