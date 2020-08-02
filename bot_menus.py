from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from models.user import get_user
from bot import bot


def render_menu(user, text, keyboard):
    """
    Edits message with inline keyboard
    that correspond to User.bot_menu_id
    """
    bot.edit_message_text(
        chat_id=user.user_id,
        message_id=user.bot_menu_id,
        text=text,
        parse_mode="HTML",
        reply_markup=keyboard
    )


def main_menu(message):
    user = get_user(message.chat.id)

    text = '<b>MAIN MENU</b>'
    
    # main menu keyboard
    keyboard = InlineKeyboardMarkup()
    keyboard.row(InlineKeyboardButton(text='🎮 Play Game', callback_data='choose_game_mode'))
    keyboard.row(InlineKeyboardButton(text='📊 Stats',     callback_data='game_stats'))
    keyboard.row(InlineKeyboardButton(text='⚙️ Settings',   callback_data='game_settings'))
    
    render_menu(user, text, keyboard)


def game_settings_menu(message):
    user = get_user(message.chat.id)

    text = '<b>game_settings_menu</b>'
    keyboard = InlineKeyboardMarkup()
    keyboard.row(InlineKeyboardButton(text='◀️ Back', callback_data='go_back'))

    render_menu(user, text, keyboard)


def game_stats_menu(message):
    user = get_user(message.chat.id)

    text = '<b>game_stats_menu</b>'
    keyboard = InlineKeyboardMarkup()
    keyboard.row(InlineKeyboardButton(text='◀️ Back', callback_data='go_back'))

    render_menu(user, text, keyboard)


def choose_game_mode_menu(message):
    user = get_user(message.chat.id)

    text = '<b>choose_game_mode_menu</b>'
    keyboard = InlineKeyboardMarkup()
    keyboard.row(InlineKeyboardButton(text='◀️ Back', callback_data='go_back'))

    render_menu(user, text, keyboard)