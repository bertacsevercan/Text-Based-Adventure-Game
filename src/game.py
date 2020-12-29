from sys import exit  # s1

char_att_dict = {}  # s2
inventory_dict = {}  # s2


def welcome():  # s1
    print(Menu.message + "\n" + Menu.options, end="=> ")


def warning_unknown_input():  # s1
    print("Unknown input! Please enter a valid one.")


class NewGame:  # s2
    char_att_list = ["1- Name => ", "2- Species => ", "3- Gender => "]
    inventory_list = ["1- Favourite Snack => ", "2- A weapon for the journey => ", "3- A traversal tool => "]

    save_file = None
    difficulty = "Medium"
    lives = 3

    def __init__(self, user_input):
        self.user_input = user_input

    def create_new_save(self):
        self.save_file = open(f"./gameSaves/{self.user_input}.txt", "w", encoding="utf-8")

    def create_char(self, user_inputs):
        self.save_file.write(user_inputs + "\n")

    def create_new_game(self):  # s2
        if self.user_input == "/quit":
            exit()
        else:
            self.create_new_save()
            print("Introduce yourself:")
            char_dict_keys = ["name", "species", "gender"]
            for i in range(len(self.char_att_list)):
                user_input = input(self.char_att_list[i])
                self.create_char(user_input)  # save the inputs to a file
                char_att_dict[char_dict_keys[i]] = user_input  # save the inputs to a dict

            print("Pack your bag for the journey:")
            inventory_dict_keys = ["snack", "weapon", "tool"]
            for j in range(len(self.inventory_list)):
                user_input = input(self.inventory_list[j])
                self.create_char(user_input)
                inventory_dict[inventory_dict_keys[j]] = user_input

            difficulty_input = input("""
Choose your difficulty:
1- Easy
2- Medium
3- Hard
=> """)
            if difficulty_input == "1" or difficulty_input.lower() == "easy":
                self.difficulty = "Easy"
                self.lives = 5
            elif difficulty_input == "2" or difficulty_input.lower() == "medium":
                self.difficulty = "Medium"
                self.lives = 3
            elif difficulty_input == "3" or difficulty_input.lower() == "hard":
                self.difficulty = "Hard"
                self.lives = 1
            else:
                warning_unknown_input()

            self.create_char(self.difficulty)
            self.create_char(str(self.lives))
            self.save_file.close()


class GameFunctions:  # s2

    def __init__(self, lives):
        self.lives = lives

    def increase_lives(self):
        self.lives += 1

    def decrease_lives(self):
        self.lives -= 1

    def show_inventory(self):
        inventory = list(inventory_dict.values())
        print(f"Inventory: {inventory}")


class Menu:  # s1, in the s1 ,the functions should be passed, they are implemeted in s2
    title = "Journey to Mount Qaf"
    message = f"***Welcome to the {title}***"
    options = """
1- Press key '1' or type 'start' to start a new game
2- Press key '2' or type 'load to load your progress
3- Press key '3' or type 'quit' to quit the game

"""

    def __init__(self, user_input):
        self.user_input = user_input

    def new_game(self):
        print("Starting a new game...")  # s1
        message = "Enter a user name to save your progress or type '/quit' to quit the game => \n"  # s2
        new_game = NewGame(input(message))
        new_game.create_new_game()

    def load_game(self):
        print("Loading your progress")  # s1


# s1
welcome()
game_menu = Menu(input())

if game_menu.user_input == "1" or game_menu.user_input.lower() == "start":
    game_menu.new_game()

elif game_menu.user_input == "2" or game_menu.user_input.lower() == "load":
    game_menu.load_game()
elif game_menu.user_input == "3" or game_menu.user_input.lower() == "quit":
    exit()
else:
    warning_unknown_input()
