from telethon import events
import os

def register(client):
    @client.on(events.NewMessage(pattern=r"\.stickerize", outgoing=True))
    async def stickerize(event):
        reply_msg = await event.get_reply_message()
        if not reply_msg or not reply_msg.media:
            await event.edit("Ответьте на сообщение с изображением.")
            return
        try:
            # Скачиваем медиафайл
            file_path = await client.download_media(reply_msg.media)
            if not file_path:
                await event.edit("Не удалось скачать изображение.")
                return

            # Отправляем как стикер
            await client.send_file(event.chat_id, file=file_path, as_sticker=True)
            await event.delete() #удаляет и сообщение с командой

            # Удаляем скачанный файл (опционально)
            os.remove(file_path)

        except Exception as e:
            await event.edit(f"Ошибка при создании стикера: {e}")