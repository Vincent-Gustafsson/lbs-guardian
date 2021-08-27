import os
import time
import requests


def send_error_message(msg):
    token = os.getenv("TELEGRAM_TOKEN")
    chat_id = os.getenv("CHAT_ID")

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    time_of_exception = time.strftime('%c')
    requests.post(url, {
        "chat_id": chat_id,
        "text": f"{time_of_exception}\n{msg}"
    })
