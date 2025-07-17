# main.py
import asyncio
from telethon import TelegramClient
from datetime import datetime
from smallfont import to_small

# — این‌ها رو از My.telegram (my.telegram.org) بگیر
API_ID = int(18479322)  # عدد API ID
API_HASH = "0a5fd8e7a6df8040dcc46b7ae8ff5576"   # رشته API HASH

# این فایل session بعد از لاگین ایجاد می‌شه:
session = "overlay_clock"

async def main():
    async with TelegramClient(session, API_ID, API_HASH) as client:
        print("✅ وارد شدی. اجرا شروع شد.")
        me = await client.get_me()
        base = me.first_name or me.username or "ᴄʀᴀᴢʏ!"

        while True:
            now = datetime.now().strftime("%H:%M")
            small = to_small(now)
            new_name = f"{base}  {small}"
            await client(functions.account.UpdateProfileRequest(first_name=new_name))
            print("🕒 نام و ساعت آپدیت شد:", new_name)
            await asyncio.sleep(60)  # هر ۶۰ ثانیه آپدیت

if __name__ == "__main__":
    asyncio.run(main())
