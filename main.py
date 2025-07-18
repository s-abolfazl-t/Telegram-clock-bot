from telethon import TelegramClient, functions
import asyncio
import datetime

api_id = 18479322
api_hash = '0a5fd8e7a6df8040dcc46b7ae8ff5576'

client = TelegramClient('overlay_clock', api_id, api_hash)

# تابع تبدیل اعداد به فونت small
def to_small(text):
    normal = "0123456789"
    small = "⁰¹²³⁴⁵⁶⁷⁸⁹"
    return "".join(small[normal.index(c)] if c in normal else c for c in text)

async def main():
    await client.start()
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        small_time = to_small(now.replace(":", ""))
        new_name = f"ᴄʀᴀᴢʏ! {small_time}"
        await client(functions.account.UpdateProfileRequest(first_name=new_name))
        await asyncio.sleep(60)

asyncio.run(main())
