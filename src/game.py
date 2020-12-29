def welcome():
    print(Menu.message + "\n" + Menu.options, end="=> ")


class Menu:
    title = "Journey to Mount Qaf"
    message = f"***Welcome to the {title}***"
    options = """
-Press key '1' to start a new game
-Press key '2' to load your progress
-Press key '3' to quit the game

"""

    def __init__(self, user_input):
        self.user_input = user_input

    def new_game(self):
        pass

    def load_game(self):
        pass

    def quit(self):
        pass


welcome()
game_menu = Menu(input())
