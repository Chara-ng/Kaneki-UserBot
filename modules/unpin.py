from telethon import events

def register(client):
    @client.on(events.NewMessage(pattern=r"\.unpin", outgoing=True))
    async def unpin_message(event):
        if event.is_group:
            try:
                await client.unpin_message(event.chat_id) #открепляет последнее
                #await client.unpin_message(event.chat_id, message=reply_msg) #открепляет конкретное reply_msg.id если указать
                await event.delete()
            except Exception as e:
                await event.edit(f"Ошибка при откреплении: {e}")
        else:
            await event.edit("Откреплять сообщения можно только в группах и каналах.")