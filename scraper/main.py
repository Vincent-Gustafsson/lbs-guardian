import os

from dotenv import load_dotenv

from get_schedules import get_schedules
from utils import cleanup, messaging


def main():
    try:
        cleanup.init_schedules_folders()

        get_schedules("student")
        get_schedules("teacher")

        cleanup.cleanup_schedules_folders()

    except Exception:
        messaging.send_error_message(
            os.environ['TELEGRAM_TOKEN'],
            os.environ['CHAT_ID']
        )


if __name__ == "__main__":
    load_dotenv()
    main()
