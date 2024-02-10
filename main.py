import os
from env import *
import telebot, wikipedia, re

bot = telebot.TeleBot(os.getenv("BOT_KEY"))
wikipedia.set_lang("tt")


# Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов
def getwiki(s):
    try:
        ny = wikipedia.page(s)
        # Получаем первую тысячу символов
        wikitext = ny.content[:1000]
        # Разделяем по точкам
        wikimas = wikitext.split(".")
        # Отбрасываем всЕ после последней точки
        wikimas = wikimas[:-1]
        # Создаем пустую переменную для текста
        wikitext2 = ""
        # Проходимся по строкам, где нет знаков «равно» (то есть все, кроме заголовков)
        for x in wikimas:
            if not ("==" in x):
                # Если в строке осталось больше трех символов, добавляем ее к нашей переменной и возвращаем утерянные при разделении строк точки на место
                if len((x.strip())) > 3:
                    wikitext2 = wikitext2 + x + "."
            else:
                break
        # Теперь при помощи регулярных выражений убираем разметку
        wikitext2 = re.sub("\([^()]*\)", "", wikitext2)
        wikitext2 = re.sub("\([^()]*\)", "", wikitext2)
        wikitext2 = re.sub("\{[^\{\}]*\}", "", wikitext2)
        # Возвращаем текстовую строку
        return wikitext2
    # Обрабатываем исключение, которое мог вернуть модуль wikipedia при запросе
    except Exception as e:
        return "Википедиядә моның турында мәгълүмат табылмады"


# Функция, обрабатывающая команду /start
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(
        m.chat.id,
        "Миңа берәр сүз җибәрсәгез, мин аның мәгънәсен Википедиядә эзләп карыйм",
    )


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):
    bot.send_message(message.chat.id, getwiki(message.text))


# Запускаем бота
bot.polling(none_stop=True, interval=0)
