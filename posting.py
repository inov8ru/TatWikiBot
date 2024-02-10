import os
from time import sleep
from env import *
from rss_parser import Parser
from requests import get
import telebot

bot = telebot.TeleBot(os.getenv("BOT_KEY"))
channel = os.getenv("CHANNEL")
filename = os.getenv("FILE")


def start_parsing():
    while True:
        parse()
        sleep(10)


def parse():
    try:
        rss_url = "https://commons.wikimedia.org/w/api.php?action=feedcontributions&user=Engelberthumperdink&newonly=1&hideminor=1&tagfilter%5B0%5D=uploadwizard&namespace=6&feedformat=rss"
        while True:
            response = get(rss_url)
            rss = Parser.parse(response.text)
            file = open(filename, "r+")
            savedLinks = [line.strip() for line in file.readlines()]
            i = 0
            for item in rss.channel.items:
                if not item.link:
                    continue
                link = item.link.replace("diff", "oldid")
                if link in savedLinks:
                    continue
                # bot.send_message(chat_id=channel, text=link)
                print("save new link {} to file".format(link))
                file.write(link + "\n")
                i = i + 1
                sleep(3)
            if i > 0:
                print("Published {} new links".format(i))
            file.close()
            sleep(20)
    except Exception as e:
        print("Error: {}".format(str(e)))
    finally:
        print("Closing file")
        file.close()
