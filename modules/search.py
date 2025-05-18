from telethon import events
from telethon.tl.functions.messages import SearchRequest
from telethon.tl.types import InputMessagesFilterEmpty

def register(client):
    @client.on(events.NewMessage(pattern=r"\.search (.*)", outgoing=True))
    async def search_messages(event):
        query = event.pattern_match.group(1)
        messages = await client(SearchRequest(
            peer=event.chat_id,
            q=query,
            filter=InputMessagesFilterEmpty(),
            min_date=None,
            max_date=None,
            offset_id=0,
            add_offset=0,
            limit=10,  # Ограничим поиск 10 сообщениями
            max_id=0,
            from_id=None,
            offset_rate=0,
            offset_peer=None,
            saved_peer=None
        ))
        if messages.messages:
            result = "Результаты поиска:\n"
            for message in messages.messages:
                result += f"- `{message.id}`: {message.message}\n"
        else:
            result = "Сообщения не найдены."
        await event.edit(result)