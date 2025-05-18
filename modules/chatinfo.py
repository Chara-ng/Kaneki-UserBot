from telethon import events

def register(client):
    @client.on(events.NewMessage(pattern=r"\.chatinfo", outgoing=True))
    async def chatinfo(event):
        chat = await event.get_chat()
        chat_id = event.chat_id
        chat_title = chat.title if hasattr(chat, 'title') else "Личный чат"  # Для личных чатов нет title
        chat_type = type(chat).__name__  # Тип чата: Channel, Chat, User
        await event.edit(
            f"**ID чата:** `{chat_id}`\n"
            f"**Название чата:** `{chat_title}`\n"
            f"**Тип чата:** `{chat_type}`"
        )