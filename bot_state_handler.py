from models.user import User, get_user, create_user
import bot_methods
from bot import bot


class BotStateHandler(object):
    """
    Implements logic of:
     -adding new users to database;
     -redirecting users to appropriate states;
     -handling '/start' command;
     -handling callbacks from inline buttons,
      which are attached to message in private chat
      between User and Bot.
    """ 
    def __init__(self):
        self.STATES = {'state_bot_start': self.state_bot_start}

    def init_states(self, states: list):
        print("\nINITIALIZING BOT STATES...\n")

        for state in states:
            self.STATES[state.__name__] = state
            print(f"{4*' '}-{state.__name__}")

        print("\nINITIALIZATION FINISHED\n")

    def state_bot_start(self, message):
        """
        Some kind of virtual method
        By default this is initial User state
        after using /start command.

        Should be implemented in BotState class
        """
        pass

    def handle_command_start(self, message):
        """
        Deletes last message with inline_keyboard
        in private chat between User and Bot and
        sends new message which will be later edited 
        with appropriate text and keyboard
        *
        If User does not exist in DB -> creates new User
        *
        Apply 'state_bot_start' for User
        """
        user = get_user(message.chat.id)

        if user:
            bot_methods.remove_message_with_inline_keyboard(message.chat.id, user.bot_menu_id)
            user.bot_menu_id = bot_methods.send_placeholder_message(message.chat.id)
            user.state = 'state_bot_start'
            user.save()
        else:
            new_user = create_user(message)
            new_user.bot_menu_id = bot_methods.send_placeholder_message(message.chat.id)
            new_user.save()

        self.STATES['state_bot_start'](message=message)

    def handle_callback(self, call):
        """
        Takes User`s callback from inline button
        and redirects it to Bot state that 
        corresponds to current User state
        """
        user = get_user(call.message.chat.id)
        self.STATES[user.state](call=call)
    
    def handle_message(self, messgae):
        """
        Takes User`s message object
        and redirects it to Bot state that 
        corresponds to current User state
        """
        user = get_user(message.chat.id)
        self.STATES[user.state](message=message)

    def switch_state_to(self, state, message=None, call=None, **kwargs):
        """
        Switches between bot states

        When user proceeds to new bot state, bot use this method
        to update User.state and call it
        """
        if state.__name__ in self.STATES:
            if message:
                User.objects(user_id=message.chat.id).update_one(state=state.__name__)
                self.STATES[state.__name__](message=message, update_menu=True)
            else:
                User.objects(user_id=call.message.chat.id).update_one(state=state.__name__)
                self.STATES[state.__name__](call=call, update_menu=True, **kwargs)
        else:
            print(f"[Warning] No state with name \"{state.__name__.upper()}\"")