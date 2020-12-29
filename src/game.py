import sys

char_att_dict = {}

def welcome():
    print(Menu.message + "\n" + Menu.options, end="=> ")


class NewGame:
    char_att_list = ["1- Name => ", "2- Species => ", "3- Gender => ", "4- Favourite Snack => ",
                     "5- A weapon for the journey => ", "6- A traversal tool => "]

    save_file = None

    def __init__(self, user_input):
        self.user_input = user_input

    def create_new_save(self):
        self.save_file = open(f"./gameSaves/{self.user_input}.txt", "w", encoding="utf-8")

    def create_char(self, user_inputs):
        self.save_file.write(user_inputs + "\n")


class Menu:
    title = "Journey to Mount Qaf"
    message = f"***Welcome to the {title}***"
    options = """
1- Press key '1' to start a new game
2- Press key '2' to load your progress
3- Press key '3' to quit the game

"""

    def __init__(self, user_input):
        self.user_input = user_input

    def new_game(self):
        print("Starting a new game...")
        message = "Enter a user name to save your progress or type '/quit' to quit the game => "
        new_game = NewGame(input(message))
        if new_game.user_input == "/quit":
            self.quit()
        else:
            new_game.create_new_save()
            dict_keys = ["name", "species", "gender", "snack", "weapon", "tool"]
            for i in range(len(new_game.char_att_list)):
                user_input = input(new_game.char_att_list[i])
                new_game.create_char(user_input)  # save the inputs to a file
                char_att_dict[dict_keys[i]] = user_input  # save the inputs to a dict
            new_game.save_file.close()
            print(char_att_dict)

    def load_game(self):
        print("Loading your progress")

    def quit(self):
        sys.exit()


welcome()
game_menu = Menu(input())

if game_menu.user_input == "1":
    game_menu.new_game()
elif game_menu.user_input == "2":
    game_menu.load_game()
elif game_menu.user_input == "3":
    game_menu.quit()
