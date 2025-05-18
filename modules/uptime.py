from telethon import events
from datetime import datetime

def register(client, start_time):  #Принимаем start_time
    @client.on(events.NewMessage(pattern=r"\.uptime", outgoing=True))
    async def uptime(event):
        now = datetime.now()
        delta = now - start_time
        await event.edit(f"Работаю уже: `{delta}`")