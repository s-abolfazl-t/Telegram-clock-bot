import asyncio
import time
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest

# === اطلاعات شخصی (از my.telegram.org بگیر) ===
API_ID = 18479322              # به عدد واقعی‌ات تغییر بده
API_HASH = '0a5fd8e7a6df8040dcc46b7ae8ff5576'   # به API HASH واقعی‌ات تغییر بده
SESSION = 'clock_session'    # هر نامی خواستی بذار (برای ساخت فایل session)
# ==============================================

# جدول تبدیل اعداد به فونت Small
small_digits = {
    '0': '₀', '1': '₁', '2': '₂', '3': '₃', '4': '₄',
    '5': '₅', '6': '₆', '7': '₇', '8': '₈', '9': '₉',
    ':': ':'
}

def to_small(text):
    return ''.join(small_digits.get(ch, ch) for ch in text)

client = TelegramClient(SESSION, API_ID, API_HASH)

async def update_name():
    await client.start()
    while True:
        now = time.strftime("%H:%M")
        small_time = to_small(now)
        try:
            await client(UpdateProfileRequest(first_name=f"{small_time} ⏰"))
            print(f"✅ نام آپدیت شد: {small_time}")
        except Exception as e:
            print("❌ خطا:", e)
        await asyncio.sleep(60)

def main():
    with client:
        client.loop.run_until_complete(update_name())

if __name__ == "__main__":
    main()