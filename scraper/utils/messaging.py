import traceback
import time
import requests


def send_error_message(token, chat_id):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    time_of_exception = time.strftime('%c')
    requests.post(url, {
        "chat_id": chat_id,
        "text": f"{time_of_exception}\n{traceback.format_exc()}"
    })
