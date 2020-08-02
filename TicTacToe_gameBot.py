from models.user import get_user
from bot_states import BotStates
from bot import bot
from config import DEV_USER_ID

class TelegramBot(object):
    def __init__(self):
        self.bot_states = BotStates()
        self.init_telegram_handlers()

    def init_telegram_handlers(self):
        @bot.message_handler(commands=['start'])
        def start(message):
            if message.chat.id == DEV_USER_ID:
                # Bot can be started only by developer(me)
                self.bot_states.handle_command_start(message)

        @bot.callback_query_handler(func=lambda call: True)
        def handle_callback(call):
            user = get_user(call.from_user.id)

            if call.message.message_id == user.bot_menu_id:
                self.bot_states.handle_callback(call)

    def run(self):
        bot.remove_webhook()
        bot.polling(none_stop=True)


if __name__ == '__main__':
    TicTacToe_gameBot = TelegramBot()
    TicTacToe_gameBot.run()