from telethon import events
import asyncio

def register(client):
    @client.on(events.NewMessage(pattern=r"\.spam (\d+) (.*)", outgoing=True))
    async def spam_message(event):
        count = int(event.pattern_match.group(1))
        text = event.pattern_match.group(2)

        if count > 10:  # Ограничение на количество сообщений
            await event.edit("Нельзя спамить больше 10 сообщений за раз.")
            return

        try:
            await event.delete()  #удаляем и сообщение с командой
            for _ in range(count):
                await client.send_message(event.chat_id, text)
                await asyncio.sleep(0.5)  # Небольшая задержка между сообщениями
        except Exception as e:
            await event.edit(f"Ошибка при спаме: {e}")