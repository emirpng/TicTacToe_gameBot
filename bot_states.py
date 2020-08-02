from bot_state_handler import BotStateHandler
import bot_menus as bot_menu
from bot import bot


class BotStates(BotStateHandler):
    """
    Class with Bot States

    Each state is a method that responsible for 
    proccesing user input (commands/callbacks)
    and applying different logic depending on it.
    """
    def __init__(self):
        super().__init__()

        self.init_states([
            self.state_main_menu,

            # main_menu:
            self.state_choose_game_mode,
            self.state_game_settings,
            self.state_game_stats,
        ])
    

    def state_bot_start(self, message):
        """
        Initial state after /start command

        Redirects User to state_main_menu
        """
        self.switch_state_to(self.state_main_menu, message)
    

    def state_main_menu(self, call=None, message=None, update_menu=False):
        """
        State shows menu with 3 inline buttons:
        -Play Game  [state_choose_game_mode]
        -Game Stats [state_game_stats]
        -Settings   [state_game_stats]

        After pressing on any of this buttons,
        User will be redirected to appropriate state
        """
        if update_menu:
            if call:
                message = call.message
            bot_menu.main_menu(message)
        else:
            if call.data == 'choose_game_mode':
                self.switch_state_to(self.state_choose_game_mode, call=call)
            elif call.data == 'game_stats':
                self.switch_state_to(self.state_game_stats, call=call)
            elif call.data == 'game_settings':
                self.switch_state_to(self.state_game_settings, call=call)

            bot.answer_callback_query(
                callback_query_id=call.id, 
                show_alert=False, 
                text=call.data
            )


    def state_choose_game_mode(self, call=None, message=None, update_menu=False):
        if update_menu:
            if call:
                message = call.message
            bot_menu.choose_game_mode_menu(message)
        else:
            if call.data == 'go_back':
                self.switch_state_to(self.state_main_menu, call=call)

            bot.answer_callback_query(
                callback_query_id=call.id, 
                show_alert=False, 
                text=call.data
            )


    def state_game_stats(self, call=None, message=None, update_menu=False):
        if update_menu:
            if call:
                message = call.message
            bot_menu.game_stats_menu(message)
        else:
            if call.data == 'go_back':
                self.switch_state_to(self.state_main_menu, call=call)

            bot.answer_callback_query(
                callback_query_id=call.id, 
                show_alert=False, 
                text=call.data
            )


    def state_game_settings(self, call=None, message=None, update_menu=False):
        if update_menu:
            if call:
                message = call.message
            bot_menu.game_settings_menu(message)
        else:
            if call.data == 'go_back':
                self.switch_state_to(self.state_main_menu, call=call)

            bot.answer_callback_query(
                callback_query_id=call.id, 
                show_alert=False, 
                text=call.data
            )
