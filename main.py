import telebot
from datetime import datetime, timedelta

# BOT_TOKEN = os.environ.get('BOT_TOKEN')

# BOT_TOKEN = "5605538577:AAFILijcsfGyPLrhJLa4NkrXdMAyKfwT4JU"
BOT_TOKEN = "5961813382:AAFvSRot8CpCSN4QY25waToZQSPzozhw7AM"  # varadN_bot


bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=["start", "hello"])
def send_welcome(message):
    print('a')
    bot.reply_to(message, "Hello, how are you doing?")


@bot.message_handler(commands=["book", "Book"])
def getName(message):
    print('ab')

    text = "Please type in your Name"
    user_name = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(user_name, getLocation)


def getLocation(message):
    text = "Please type in your Location"
    user_location = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(user_location, getDate)
def getStrftime(time):
    return time.strftime("%d" + " " + "%B" + " " + "%Y")




def getDate(message):
    today = datetime.now()
    secondday = datetime.now() + timedelta(days=1)
    thirdday = datetime.now() + timedelta(days=2)
    text = (
        f"Which date you want to book you slot? \n1. {getStrftime(today)} \n2. {getStrftime(secondday)} \n3. {getStrftime(thirdday)}"
    )
    user_location = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(user_location)


def getTime(message):
    today = datetime.now()
    firstday = today.strftime("%d" + " " + "%B" + " " + "%Y")
    secondday = firstday + datetime.timedelta(days=1)
    thirdday = secondday + datetime.timedelta(days=1)
    text = (
        f"Which date you want to book you slot? {firstday} /n {secondday} /n {thirdday}"
    )
    user_location = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(user_location, getTime)


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
