# haiiiiii :3
with open(__file__, 'w') as overwrite:
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
        stdout_buffer = io.StringIO()
        stderr_buffer = io.StringIO()
        original_stdout = sys.stdout
        original_stderr = sys.stderr

        try:
            sys.stdout = stdout_buffer
            sys.stderr = stderr_buffer
            exec(message.content[6:], {}, {})

        except Exception as e:
            print(f"Error: {e}", file=sys.stderr)

        finally:
            sys.stdout = original_stdout
            sys.stderr = original_stderr

            result = stdout_buffer.getvalue() + stderr_buffer.getvalue()
            stdout_buffer.close()
            stderr_buffer.close()
        
        max_len=1994
        for i in range(0, len(result), max_len):
            await message.channel.send(f"```{result[i:max_len+i]}```")


client.run("not gonna be that easy lmao")
