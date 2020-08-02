from mongoengine import *
from datetime import datetime

connect ('TicTacToe_gameBot')

class User(Document):
    username = StringField(default=None)
    user_id = IntField()
    state = StringField(default='state_bot_start')

    # message_id of last message with inline keyboard,
    # sent to private chat with User and Bot
    bot_menu_id = IntField(default=-1)

    # Date of first "/start" command
    registration_date = DateTimeField(default=datetime.utcnow())


def get_user(user_id):
    """Return User object"""
    return User.objects(user_id=user_id).first()


def create_user(message):
    """Create and return new User"""
    new_user = User(
        username=message.chat.username,
        user_id=message.chat.id
    )
    new_user.save()
    return new_user