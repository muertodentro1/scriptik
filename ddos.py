import asyncio
from telethon import TelegramClient, events, sync

# Замените эти значения на свои собственные данные
api_id = '24751341'
api_hash = '56a72909d637e1c365425e5ea8e4fa10'
phone_number = '79964088609'

# Создаем клиент для подключения к Telegram
client = TelegramClient(phone_number, api_id, api_hash)

async def main():
    await client.start()
    print("Client Created")

    # Получаем "Saved Messages"
    saved_messages = await client.get_entity('me')
    
    # Получаем последнее сообщение из "Saved Messages"
    last_message = await client.get_messages(saved_messages, limit=1)
    message_to_send = last_message[0].message
    photo_to_send = last_message[0].media if last_message[0].media else None

    # Получаем все диалоги и фильтруем их по названию папки
    folder_name = "face"  # Замените на название вашей папки
    all_dialogs = await client.get_dialogs()
    target_dialogs = [d for d in all_dialogs if d.folder and d.folder.name == folder_name]

    # Отправляем сообщение и фото в каждый чат в папке
    for dialog in target_dialogs:
        await client.send_message(dialog.id, message_to_send, file=photo_to_send)
        print(f"Message and photo sent to {dialog.name}")

# Запускаем скрипт
asyncio.run(main())