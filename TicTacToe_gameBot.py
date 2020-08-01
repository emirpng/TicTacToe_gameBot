from bot import bot


class TicTacToe_gameBot(object):
    def __init__(self):
        self.run_handlers()

    def run_handlers(self):
        @bot.message_handler(commands=['start'])
        def start(message):
            self.print_user_message_text(message)
            bot.send_message(
                chat_id=message.chat.id,
                text='Welcome to TicTacToe_gameBot!'
            )

        @bot.message_handler(content_types=['text'])   
        def reply_to_user_message(message):
            self.print_user_message_text(message)
            bot.reply_to(
                message=message,
                text='TicTacToe_gameBot 🔥'
            )

    def print_user_message_text(self, message):
        if (username := message.from_user.username):
            print(f"@{username} > {message.text}")
        else:
            print(f"User '{message.from_user.id}' > {message.text}")

    def run(self):
        bot.remove_webhook()
        bot.polling(none_stop=True)


if __name__ == '__main__':
    try:
        telegram_bot = TicTacToe_gameBot()
        telegram_bot.run()
    except Exception as e:
        print(e)