from telethon import TelegramClient, functions
from smallfont import to_small
import asyncio
import datetime

api_id = 18479322  # عدد api_id خودت رو اینجا بذار
api_hash = '0a5fd8e7a6df8040dcc46b7ae8ff5576'  # رشته api_hash خودت رو اینجا بذار

client = TelegramClient('overlay_clock', api_id, api_hash)

async def main():
    await client.start()
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        small_time = to_small(now)
        new_name = f"ᴄʀᴀᴢʏ! {small_time}"
        await client(functions.account.UpdateProfileRequest(first_name=new_name))
        await asyncio.sleep(60)

asyncio.run(main())
