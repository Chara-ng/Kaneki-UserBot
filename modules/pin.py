from telethon import events

def register(client):
    @client.on(events.NewMessage(pattern=r"\.pin", outgoing=True))
    async def pin_message(event):
        if event.is_group:  # Пин можно только в группах/каналах
            reply_msg = await event.get_reply_message()
            if reply_msg:
                try:
                    await client.pin_message(event.chat_id, reply_msg.id)
                    await event.delete()
                except Exception as e:
                    await event.edit(f"Ошибка при закреплении: {e}")
            else:
                await event.edit("Ответьте на сообщение, которое хотите закрепить.")
        else:
            await event.edit("Закреплять сообщения можно только в группах и каналах.")