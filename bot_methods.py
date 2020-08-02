from bot import bot
from models.user import get_user


def remove_message_with_inline_keyboard(chat_id, message_id):
    try:
        bot.delete_message(
            chat_id=chat_id,
            message_id=message_id
        )
    except Exception as e:
        # if 48hrs limit for deleting has expired
        try:
            bot.edit_message_text(
                chat_id=chat_id,
                message_id=message_id,
                text="😴",
            )
        except Exception as e:
            # if BOT can`t find message to edit or u
            # nknown issue occured, pass
            pass


def send_placeholder_message(chat_id):
    """
    sends message, which will be editted
    with inline keyboard in further states

    return message_id (int) of sent message
    """

    message_id = bot.send_message(
        chat_id=chat_id,
        text="⏳",
    ).message_id

    return message_id