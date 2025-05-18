from telethon import events
import time

def register(client):
    @client.on(events.NewMessage(pattern=r"\.ping", outgoing=True))
    async def ping(event):
        start = time.time()
        msg = await event.edit("`Pong!`")
        end = time.time()
        latency = round((end - start) * 1000, 2)
        await msg.edit(f"Понг!\nЗадержка: `{latency}ms`")