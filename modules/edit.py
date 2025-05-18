from telethon import events

def register(client):
    @client.on(events.NewMessage(pattern=r"\.edit (.*)", outgoing=True))
    async def edit_message(event):
        reply_msg = await event.get_reply_message()
        if reply_msg:
            new_text = event.pattern_match.group(1)
            try:
                await client.edit_message(entity=event.chat_id, message=reply_msg.id, text=new_text)
                await event.delete() #удаляет и сообщение с командой
            except Exception as e:
                await event.edit(f"Ошибка при редактировании: {e}")
        else:
            await event.edit("Ответьте на сообщение, которое хотите редактировать.")