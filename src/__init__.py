import threading
from telegram import Telegram


if __name__ == "__main__":
    threads = []

    telegram = threading.Thread(target=Telegram().execute)
    threads.append(telegram)
    telegram.start()

    for t in threads:
        t.join()
