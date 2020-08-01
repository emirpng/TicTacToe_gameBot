import os
import telebot


BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    print_user_message_text(message)
    bot.send_message(
        chat_id=message.chat.id,
        text='Welcome to TicTacToe_gameBot!'
    )


@bot.message_handler(content_types=['text'])   
def reply_to_user_message(message):
    print_user_message_text(message)
    bot.reply_to(
        message=message,
        text='TicTacToe_gameBot 🔥'
    )


def print_user_message_text(message):
    if (username := message.from_user.username):
        print(f"@{username} > {message.text}")
    else:
        print(f"User '{message.from_user.id}' > {message.text}")
    


if __name__ == '__main__':
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f'[ERROR] {e}')