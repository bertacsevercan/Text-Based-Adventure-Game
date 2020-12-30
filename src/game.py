from sys import exit  # s1


def welcome():  # s1
    title = "Journey to Mount Qaf"
    print(f"***Welcome to the {title}***")


def warning_unknown_input():  # s1
    print("Unknown input! Please enter a valid one.")


class Game:  # s2
    """
    Gonna save this game_state to the file and then read it in load game. As long as the attributes are updated
    it's ok
    """
    char_att_dict = {}
    inventory_dict = {}
    difficulty = "Medium"
    lives = 3
    level = 1


class NewGame(Game):  # s2
    char_att_list = ["1- Name => ", "2- Species => ", "3- Gender => "]
    inventory_list = ["1- Favourite Snack => ", "2- A weapon for the journey => ", "3- A traversal tool => "]
    save_file = None

    def __init__(self, username_input):
        self.username_input = username_input

    def create_new_save(self):
        self.save_file = open(f"./gameSaves/{self.username_input}.txt", "w", encoding="utf-8")

    def create_char(self, user_inputs):
        self.save_file.write(user_inputs + "\n")

    def create_new_game(self):  # s2
        self.create_new_save()
        print("Create your character:")
        char_dict_keys = ["name", "species", "gender"]
        for i in range(len(self.char_att_list)):
            user_input = input(self.char_att_list[i])
            self.create_char(user_input)  # save the inputs to a file
            self.char_att_dict[char_dict_keys[i]] = user_input  # save the inputs to a dict

        print("Pack your bag for the journey:")
        inventory_dict_keys = ["snack", "weapon", "tool"]
        for j in range(len(self.inventory_list)):
            user_input = input(self.inventory_list[j])
            self.create_char(user_input)
            self.inventory_dict[inventory_dict_keys[j]] = user_input

        print("""Choose your difficulty:
1- Easy
2- Medium
3- Hard""")
        while True:
            difficulty_input = input("=> ")
            if difficulty_input == "1" or difficulty_input.lower() == "easy":
                self.difficulty = "Easy"
                self.lives = 5
                break
            elif difficulty_input == "2" or difficulty_input.lower() == "medium":
                self.difficulty = "Medium"
                self.lives = 3
                break
            elif difficulty_input == "3" or difficulty_input.lower() == "hard":
                self.difficulty = "Hard"
                self.lives = 1
                break
            else:
                warning_unknown_input()

        self.create_char(self.difficulty)
        self.create_char(str(self.lives))
        self.save_file.close()
        print("Good luck on your journey " + self.char_att_dict["name"])


class GameFunctions(Game):  # s2

    def increase_lives(self):
        self.lives += 1

    def decrease_lives(self):
        self.lives -= 1

    def show_inventory(self):
        inventory = ", ".join(list(self.inventory_dict.values()))
        print(f"Inventory: {inventory}")

    def add_item(self, item):
        self.inventory_dict[item] = item

    def remove_item(self, item):
        self.inventory_dict[item].pop()

    def gameplay(self, story, choice1, choice2, choice3, outcome1, outcome2, outcome3,
                 func1=None, param1=None, func2=None, param2=None, func3=None, param3=None):  # s3
        """Trying to make this reusable as possible!!!"""
        input_message = f"""{story}
        
What will you do? Type the number of the option or type '/i' to check your inventory.

1- {choice1}
2- {choice2}
3- {choice3}"""
        print(input_message)
        while True:
            action_input = input("=> ")
            if action_input == "1":
                print(outcome1)
                return func1(param1)
            elif action_input == "2":
                print(outcome2)
                return func2(param2)
            elif action_input == "3":
                print(outcome3)
                return func3(param3)
            elif action_input == "/i":
                self.show_inventory()
            elif action_input == "/q":
                exit_message = "You sure you want to quit to menu: Y/N: ?"
                if exit_message.lower() == "y":
                    print("Goodbye!")
                    break
                else:
                    continue
            else:
                warning_unknown_input()


class Menu:  # s1, in the s1 ,the functions should be passed, they are implemeted in s2

    options = """
1- Press key '1' or type 'start' to start a new game
2- Press key '2' or type 'load to load your progress
3- Press key '3' or type 'quit' to quit the game"""

    def __init__(self, user_input):
        self.user_input = user_input

    def show_options(self):
        print(self.options)

    def new_game(self):
        print("Starting a new game...")  # s1
        message = "Enter a user name to save your progress or type '/b' to go back => "  # s2
        new_game = NewGame(input(message))
        while True:
            if new_game.username_input == "/b":
                print("Going back to menu...")
                break
            else:
                new_game.create_new_game()
                helper.gameplay(sample_txt[0], sample_txt[1], sample_txt[2], sample_txt[3],  # s3
                        "You found a key.", f"You used {helper.inventory_dict['tool']} to go up a bit.",
                        "You admired the majestic view of the mountain!", helper.add_item, "Key")
                helper.show_inventory()
                break

    def load_game(self):
        print("Loading your progress")  # s1


sample_txt = ["""Once you reach the beginning of the Mount Qaf, you feel amazed by the majestic 
mountain that you will conquer at the end of this climb. You look at the snowy peaks while 
thinking of how to start the journey. There is a hill before you.""",
              "Walk around a bit, maybe you'll find something interesting.",  # s3
              "Walk up the hill and begin climbing.",
              "Enjoy the scenery."]

# s1
welcome()
game_menu = Menu(None)
helper = GameFunctions()  # s2
while True: #s1
    game_menu.show_options()
    game_menu.user_input = input("=> ")
    if game_menu.user_input == "1" or game_menu.user_input.lower() == "start":
        game_menu.new_game()
    elif game_menu.user_input == "2" or game_menu.user_input.lower() == "load":
        game_menu.load_game()
        break
    elif game_menu.user_input == "3" or game_menu.user_input.lower() == "quit":
        break
    else:
        warning_unknown_input()
