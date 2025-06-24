
import requests
import time
import os
from telegram import Bot

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_NAME = os.environ.get("CHANNEL_NAME")
bot = Bot(token=BOT_TOKEN)

def get_volume(coin="KRW-BTC"):
    url = f"https://api.upbit.com/v1/ticker?markets={coin}"
    response = requests.get(url)
    data = response.json()[0]
    return data['acc_trade_volume_24h'], data['trade_price']

last_volume = 0
while True:
    try:
        volume, price = get_volume()
        if last_volume != 0 and volume > last_volume * 1.2:
            bot.send_message(chat_id=CHANNEL_NAME, text=f"📈 거래량 급등!\n현재 가격: {price:,}원")
        last_volume = volume
    except Exception as e:
        print("에러 발생:", e)
    time.sleep(60)
