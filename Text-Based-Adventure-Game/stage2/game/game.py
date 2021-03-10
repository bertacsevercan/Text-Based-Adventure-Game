from termcolor import cprint, colored


def warning_unknown_input():
    cprint("Unknown input! Please enter a valid one.", "red")


class Game:
    char_att_dict = {}
    inventory_dict = {}
    difficulty = "Medium"
    lives = 3
    level = 1
    isAlive = True
    save_file_path = None


class NewGame:
    char_att_list = ["1- Name => ", "2- Species => ", "3- Gender => "]
    inventory_list = ["1- Favourite Snack => ", "2- A weapon for the journey => ", "3- A traversal tool => "]
    char_dict_keys = ["name", "species", "gender"]
    inventory_dict_keys = ["snack", "weapon", "tool"]

    def __init__(self, username_input):
        self.username_input = username_input

    def create_new_game(self):

        Game.save_file_path = f"./saves/{self.username_input}.txt"

        cprint("Create your character:", "yellow", attrs=["bold", "underline"])

        for i in range(len(self.char_att_list)):
            user_input = input(colored(self.char_att_list[i], "magenta", attrs=["bold"])).title()
            Game.char_att_dict[self.char_dict_keys[i]] = user_input

        cprint("Pack your bag for the journey:", "yellow", attrs=["bold", "underline"])

        for j in range(len(self.inventory_list)):
            user_input = input(colored(self.inventory_list[j], "magenta", attrs=["bold"])).title()
            Game.inventory_dict[self.inventory_dict_keys[j]] = user_input

        cprint("Choose your difficulty:", "yellow", attrs=["bold", "underline"])
        cprint("1- Easy\n2- Medium\n3- Hard", "magenta", attrs=["bold"])

        while True:
            difficulty_input = input()
            if difficulty_input == "1" or difficulty_input.lower() == "easy":
                Game.difficulty = "Easy"
                Game.lives = 5
                break
            elif difficulty_input == "2" or difficulty_input.lower() == "medium":
                Game.difficulty = "Medium"
                Game.lives = 3
                break
            elif difficulty_input == "3" or difficulty_input.lower() == "hard":
                Game.difficulty = "Hard"
                Game.lives = 1
                break
            else:
                warning_unknown_input()

        cprint("Good luck on your journey:", "cyan", attrs=["bold"])

        print(f"Your character: {', '.join(Game.char_att_dict.values())}")
        print(f"Your inventory: {', '.join(Game.inventory_dict.values())}")
        print("Difficulty: " + Game.difficulty)


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
        message = colored("Enter a user name to save your progress or type '/b' to go back => ", "magenta",
                          attrs=["bold"])
        new_game = NewGame(input(message))
        while True:
            if new_game.username_input.lower() == "/b":
                cprint("Going back to menu...", "blue")
                break
            else:
                new_game.create_new_game()
            break  # go back to menu

    def load_game(self):
        cprint("No save data found!", "blue")


game_menu = Menu(None)

while True:

    Menu.welcome()

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
