from telethon import events

def register(client):
    @client.on(events.NewMessage(pattern=r"\.forward", outgoing=True))
    async def forward_message(event):
        reply_msg = await event.get_reply_message()
        if reply_msg:
            try:
                await client.forward_messages(entity=event.chat_id, messages=reply_msg) #пересылаем в тот же чат
                await event.edit(f"Сообщение переслано в этот же чат.")
            except Exception as e:
                await event.edit(f"Ошибка при пересылке: {e}")
        else:
            await event.edit("Ответьте на сообщение, которое хотите переслать.")