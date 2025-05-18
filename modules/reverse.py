from telethon import events
import os
import subprocess

def register(client):
    @client.on(events.NewMessage(pattern=r"\.reverse", outgoing=True))
    async def reverse_media(event):
        reply_msg = await event.get_reply_message()
        if not reply_msg or not reply_msg.media:
            await event.edit("Ответьте на сообщение с видео или GIF.")
            return

        try:
            # Скачиваем медиафайл
            file_path = await client.download_media(reply_msg.media)
            if not file_path:
                await event.edit("Не удалось скачать видео/GIF.")
                return

            # Проверяем, установлен ли ffmpeg
            try:
                subprocess.run(["ffmpeg", "-version"], check=True, capture_output=True)
            except FileNotFoundError:
                await event.edit("FFmpeg не установлен. Он необходим для разворота видео.")
                return

            # Создаем перевернутое видео
            output_path = "reversed_" + os.path.basename(file_path)
            command = [
                "ffmpeg",
                "-i", file_path,
                "-vf", "reverse",
                output_path
            ]
            subprocess.run(command, check=True)

            # Отправляем перевернутое видео
            await client.send_file(event.chat_id, file=output_path)
            await event.delete() #удаляет и сообщение с командой

            # Удаляем скачанный и перевернутый файлы (опционально)
            os.remove(file_path)
            os.remove(output_path)

        except Exception as e:
            await event.edit(f"Ошибка при развороте видео: {e}")