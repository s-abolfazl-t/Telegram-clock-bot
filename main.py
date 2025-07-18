import asyncio
from telethon import TelegramClient
from datetime import datetime

# اطلاعات اکانت تلگرام (از https://my.telegram.org بگیر)
API_ID = "18479322"
API_HASH = "0a5fd8e7a6df8040dcc46b7ae8ff5576"
PHONE_NUMBER = "+989035930856"  # مثلاً: +989123456789

# دیکشنری برای تبدیل اعداد به یونیکد اسمال
UNICODE_SMALL_DIGITS = {
    '0': '𝟶', '1': '𝟷', '2': '𝟸', '3': '𝟹', '4': '𝟺',
    '5': '𝟻', '6': '𝟼', '7': '𝟽', '8': '𝟾', '9': '𝟿'
}

def to_small_digits(time_str):
    """تبدیل اعداد به فونت یونیکد اسمال"""
    return ''.join(UNICODE_SMALL_DIGITS.get(char, char) for char in time_str)

async def update_name(client):
    while True:
        try:
            # گرفتن زمان فعلی به فرمت HH:MM
            current_time = datetime.now().strftime("%H:%M")
            # تبدیل زمان به فونت یونیکد اسمال
            small_time = to_small_digits(current_time)
            # آپدیت اسم نمایشی
            await client(UpdateProfileRequest(
                first_name=f"مهدی | {small_time}"
            ))
            print(f"اسم آپدیت شد: مهدی | {small_time}")
            # صبر 60 ثانیه تا آپدیت بعدی
            await asyncio.sleep(60)
        except Exception as e:
            print(f"خطا: {e}")
            await asyncio.sleep(5)  # درصورت خطا، 5 ثانیه صبر کن

async def main():
    # اتصال به اکانت تلگرام
    client = TelegramClient('session_name', API_ID, API_HASH)
    await client.start(phone=PHONE_NUMBER)
    print("به تلگرام متصل شد!")
    await update_name(client)

if __name__ == "__main__":
    asyncio.run(main())
