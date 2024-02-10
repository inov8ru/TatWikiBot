from threading import Thread
from bot import start_bot
from posting import start_parsing

threads = [
    Thread(target=start_bot, name="bot"),
    Thread(target=start_parsing, name="parsing"),
]

for t in threads:
    t.start()

print("Script was started")

for t in threads:
    t.join()
