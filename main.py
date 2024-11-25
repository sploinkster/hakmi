# timeout login is sillypass btw :333
with open("main.py", 'w') as overwrite:
    overwrite.write("no peeking! :3")

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
        output = io.StringIO()
        old_stdout = sys.stdout
        sys.stdout = output

        exec(message.content[6:])

        sys.stdout = old_stdout
        result = output.getvalue()
        output.close()
        
        max_len=1994
        for i in range(0, len(result), max_len):
            await message.channel.send(f"```{result[i:max_len+i]}```")


client.run("token goes here")
