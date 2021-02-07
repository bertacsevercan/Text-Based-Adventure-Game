from termcolor import cprint, colored
from re import sub
import os

file_path = (os.path.dirname(__file__))

story_container = ""
with open(file_path + "/story/story.txt") as story_f:
    for line in story_f:
        story_container += line
story_list = story_container.split("+")

choices = []
with open(file_path + "/story/choices.txt") as choices_f:
    for line in choices_f:
        choices.append(sub(r"{.*}", "", line.strip()))

outcome_container = ""
with open(file_path + "/story/outcomes.txt") as outcomes_f:
    for line in outcomes_f:
        outcome_container += sub(r"({.*})|(\(.*\))", "", line.strip())
outcomes = outcome_container.split("*")


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
    char_att_list = ["1- Name =", "2- Species =", "3- Gender ="]
    inventory_list = ["1- Favourite Snack =", "2- A weapon for the journey =", "3- A traversal tool ="]
    char_dict_keys = ["name", "species", "gender"]
    inventory_dict_keys = ["snack", "weapon", "tool"]

    def __init__(self, username_input):
        self.username_input = username_input

    def create_new_game(self):

        Game.save_file_path = f"{file_path}/saves/{self.username_input}.txt"

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


class Helper:

    @staticmethod
    def increase_lives():
        Game.lives += 1
        print(colored("You gained an extra life! Life count: ", "green", attrs=["bold"]), Game.lives)

    @staticmethod
    def decrease_lives():
        Game.lives -= 1
        Game.isAlive = False
        print(colored("You died! Life count: ", "red", attrs=["bold"]), Game.lives)

    @staticmethod
    def show_inventory():
        inventory = ", ".join(list(Game.inventory_dict.values()))
        cprint(f"Inventory: {inventory}", "cyan")

    @staticmethod
    def add_item(item):
        Game.inventory_dict[item] = item.title()
        cprint("A new item has been added to your inventory: " + Game.inventory_dict[item], "red", attrs=["bold"])

    @staticmethod
    def remove_item(item):
        cprint("An item has been removed from your inventory: " + Game.inventory_dict[item], "red", attrs=["bold"])
        Game.inventory_dict.pop(item)

    @staticmethod
    def show_char():
        char = ", ".join(list(Game.char_att_dict.values()))
        lives = Game.lives
        cprint(f"Your character: {char}.\nLife count: {lives}", "cyan")

    @staticmethod
    def show_help():
        cprint("Type the number of the option you want to choose.\n" +
               "Commands you can use:\n/i => Shows inventory.\n" +
               "/q => Exits the game.\n" +
               "/c => Shows character traits.\n" +
               "/h => Shows help.", "blue")

    @staticmethod
    def game_won():
        print("Congratulations! You beat the game!")
        exit()

    @staticmethod
    def load_inventory():
        with open(Game.save_file_path, "r") as f:
            content = f.readlines()
            inventory = content[1].strip().split(",")

            for i in range(len(inventory)):
                Game.inventory_dict[NewGame.inventory_dict_keys[i]] = inventory[i]

    @staticmethod
    def save_game():
        cprint("You've found a safe spot to rest. Saving your progress...", "yellow", attrs=["bold"])
        inventory = ", ".join(list(Game.inventory_dict.values()))
        char_attrs = ", ".join(list(Game.char_att_dict.values()))
        Game.level += 1
        with open(Game.save_file_path, "w") as f:
            writings = [char_attrs + "\n", inventory + "\n", str(Game.difficulty) + " ", str(Game.lives) + "\n",
                        str(Game.level) + "\n"]
            f.writelines(writings)

    @staticmethod
    def gameplay(story, choice1, choice2, choice3, outcome1, outcome2, outcome3,
                 func1=None, param1=None, func2=None, param2=None, func3=None, param3=None):

        input_message = f"""What will you do? Type the number of the option or type '/h' to show help.

1- {choice1}
2- {choice2}
3- {choice3}"""
        cprint(story, "cyan", attrs=["bold"])
        cprint(input_message, "magenta", attrs=["bold"])
        while True:
            action_input = input(colored("=> ", "green", attrs=["bold"]))
            if action_input == "1":
                cprint(outcome1, "green", attrs=["bold"])
                if func1 is not None:
                    if param1 is None:
                        return func1()
                    return func1(param1)
                else:
                    continue
            elif action_input == "2":
                cprint(outcome2, "green", attrs=["bold"])
                if func2 is not None:
                    if param2 is None:
                        return func2()
                    return func2(param2)
                else:
                    continue
            elif action_input == "3":
                cprint(outcome3, "green", attrs=["bold"])
                if func3 is not None:
                    if param3 is None:
                        return func3()
                    return func3(param3)
                else:
                    continue
            elif action_input.lower() == "/h":
                Helper.show_help()
            elif action_input.lower() == "/c":
                Helper.show_char()
            elif action_input.lower() == "/i":
                Helper.show_inventory()
            elif action_input.lower() == "/q":
                message = colored("You sure you want to quit the game? Y/N => ", "magenta", attrs=["bold"])
                exit_input = input(message)
                if exit_input.lower() == "y":
                    cprint("Goodbye!", "blue")
                    exit()
                else:
                    continue
            else:
                warning_unknown_input()


class Levels:

    @staticmethod
    def core_game_loop():
        while True:
            if Game.lives > 0:
                if Game.level == 1:
                    Levels.level1()
                elif Game.level == 2:
                    Levels.level2()
                else:
                    cprint("Oops! Something went wrong.", "red", attrs=["bold"])
                    break
            else:
                cprint("You ran out of lives! Game over!", "red", attrs=["bold"])
                break

    @staticmethod
    def level1():
        while True:
            cprint(story_list[0], "yellow", attrs=["bold", "underline"])
            Game.isAlive = True

            Helper.gameplay(story_list[1], choices[0], choices[1], choices[2],
                            outcomes[0],
                            outcomes[1] + Game.inventory_dict['tool'],
                            outcomes[2], Helper.add_item, "key", print)

            Helper.gameplay(story_list[2], choices[3], choices[4], choices[5],
                            outcomes[3] if "key" in Game.inventory_dict
                            else outcomes[4],
                            outcomes[5],
                            outcomes[6], Helper.remove_item if "key" in Game.inventory_dict
                            else None, "key", func3=Helper.decrease_lives)
            if not Game.isAlive:
                break

            Helper.gameplay(story_list[3], choices[6], choices[7], choices[8],
                            outcomes[7],
                            outcomes[8],
                            outcomes[9],
                            Helper.decrease_lives, func2=Helper.decrease_lives,
                            func3=Helper.save_game)
            if not Game.isAlive:
                break
            if Game.level == 2:
                break

    @staticmethod
    def level2():
        while True:
            Helper.load_inventory()
            cprint(story_list[4], "yellow", attrs=["bold", "underline"])
            Game.isAlive = True

            Helper.gameplay(story_list[5], choices[9], f"{choices[10]} {Game.inventory_dict['weapon']}.", choices[11],
                            outcomes[10],
                            outcomes[11],
                            outcomes[12], func2=print, func3=Helper.remove_item, param3="snack")

            Helper.gameplay(story_list[6], choices[12], choices[13], choices[14],
                            outcomes[13], outcomes[14], outcomes[15],
                            Helper.increase_lives, func2=Helper.decrease_lives, func3=print)
            if not Game.isAlive:
                break

            Helper.gameplay(story_list[7], choices[15], f"{choices[16]} {Game.inventory_dict['weapon']}", choices[17],
                            outcomes[16],
                            outcomes[17],
                            outcomes[18] if 'snack' not in Game.inventory_dict else
                            outcomes[19],
                            Helper.decrease_lives, func2=Helper.decrease_lives,
                            func3=Helper.game_won if 'snack' not in Game.inventory_dict else Helper.decrease_lives)
            if not Game.isAlive:
                break


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
        message = colored("Enter a user name to save your progress or type '/b' to go back ", "magenta",
                          attrs=["bold"])
        new_game = NewGame(input(message))
        while True:
            if new_game.username_input.lower() == "/b":
                cprint("Going back to menu...", "blue")
                break
            else:
                new_game.create_new_game()
                Levels.core_game_loop()
            break  # go back to menu

    def load_game(self):
        try:
            saves = list(map(lambda x: x.replace(".txt", ""), os.listdir(f'{file_path}/saves/')))  # get rid of .txt
            cprint("Type your username from the list:", "yellow")
            for save in saves:
                cprint(save, "magenta", attrs=["bold"])
            path = input(colored("=> ", "green", attrs=["bold"]))
            Game.save_file_path = f'{file_path}/saves/{path}.txt'
            with open(Game.save_file_path) as f:
                cprint("Loading your progress...", "blue")  # s1 #s3
                content = f.readlines()

                char = content[0].strip().split(",")

                inventory = content[1].strip().split(",")

                for i in range(len(char)):
                    Game.char_att_dict[NewGame.char_dict_keys[i]] = char[i]
                    Game.inventory_dict[NewGame.inventory_dict_keys[i]] = inventory[i]

                difficulty = content[2].strip().split()
                Game.difficulty = difficulty[0]
                Game.lives = int(difficulty[1])

                level = int(content[3].strip())
                Game.level = level

                Levels.core_game_loop()

        except (TypeError, IndexError, FileNotFoundError):
            cprint("No save data found!", "red", attrs=["bold"])


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
