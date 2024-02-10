from threading import Thread
from bot import start_bot
from posting import start_parsing

threads = [
    Thread(target=start_bot, daemon=True, name="bot"),
    Thread(target=start_parsing, daemon=True, name="parsing"),
]

for t in threads:
    t.start()

for t in threads:
    t.join()
