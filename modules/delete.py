from telethon import events

def register(client):
    @client.on(events.NewMessage(pattern=r"\.delete", outgoing=True))
    async def delete_message(event):
        reply_msg = await event.get_reply_message()
        if reply_msg:
            try:
                await reply_msg.delete()
                await event.delete()  #удаляет и сообщение с командой
            except Exception as e:
                await event.edit(f"Ошибка при удалении: {e}")
        else:
            await event.edit("Ответьте на сообщение, которое хотите удалить.")