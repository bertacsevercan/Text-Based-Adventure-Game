from termcolor import cprint, colored


def warning_unknown_input():
    cprint("Unknown input! Please enter a valid one.", "red")


class Menu:
    options = """
    
1- Press key '1' or type 'start' to start a new game
2- Press key '2' or type 'load' to load your progress
3- Press key '3' or type 'quit' to quit the game"""

    def __init__(self, user_input):
        self.user_input = user_input

    @staticmethod
    def welcome():
        title = "Journey to Mount Qaf"
        print(colored(f"\n***Welcome to the {title}***", "yellow", attrs=["bold"]),
              colored(Menu.options, "magenta", attrs=["bold"]))

    def new_game(self):
        cprint("Starting a new game...", "blue")

    def load_game(self):
        cprint("No save data found!", "blue")


game_menu = Menu(None)

Menu.welcome()

while True:

    game_menu.user_input = input()

    if game_menu.user_input == "1" or game_menu.user_input.lower() == "start":
        game_menu.new_game()

    elif game_menu.user_input == "2" or game_menu.user_input.lower() == "load":
        game_menu.load_game()

    elif game_menu.user_input == "3" or game_menu.user_input.lower() == "quit":
        cprint("Goodbye!", "blue")
        break

    else:
        warning_unknown_input()
