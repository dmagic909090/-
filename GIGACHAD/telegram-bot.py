import telebot
from time import sleep
from BOT import TOKEN

bot = telebot.TeleBot(TOKEN)

# Dictionary to store user states
user_states = {}

# Constants for user states
ASKED_HOW_ARE_YOU = "asked_how_are_you"

@bot.message_handler(content_types=['text'])
def text(message):
    user_id = message.from_user.id
    text = message.text.lower()

    if text == "привет":
        bot.send_message(user_id, 'привет ')
        # Note: Telegram bots cannot use input() to get responses directly.
        # We can set up a state to handle the next message instead.
        bot.send_message(user_id, 'как тебя зовут?')
        user_states[user_id] = 'asking_name'


    elif text == "как дела":
        sleep(1)
        bot.send_message(user_id, 'хорошо ')
        sleep(3)
        bot.send_message(user_id, 'а у тебя?')
        user_states[user_id] = ASKED_HOW_ARE_YOU

    elif user_states.get(user_id) == 'asking_name':
        bot.send_message(user_id, f'Приятно познакомиться, {message.text}!')
        user_states[user_id] = None

    elif user_states.get(user_id) == ASKED_HOW_ARE_YOU:
        if "хорошо" in text or "отлично" in text:
            bot.send_message(user_id, "Рад это слышать!")
        elif "плохо" in text or "не очень" in text:
            bot.send_message(user_id, "Жаль это слышать. Надеюсь, все наладится.")
        else:
            bot.send_message(user_id, "Понятно. Спасибо за ответ.")
        user_states[user_id] = None

    elif text == 'хорошо':
        sleep(1)
        bot.send_message(user_id, "отлично")

    elif "hello" in text or "hi" in text:
            bot.send_message(user_id, "hello" + {message.text})

    elif text == "пока":
        sleep(1)
        bot.send_message(user_id, 'до встречи  ')

    elif text == "что делаеш":
        sleep(1)
        bot.send_message(user_id, 'разговариваю с тобой')

    elif text == "/start":
        sleep(1)
        bot.send_message(user_id, 'добро пожаловать в мой телеграм бот  ')

    else:
        bot.send_message(user_id, 'чё ?')
        sleep(1)
        bot.send_message(user_id, 'у тебя всё хорошо ?')

bot.infinity_polling()
