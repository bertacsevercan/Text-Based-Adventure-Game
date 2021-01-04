from sys import exit  # s1
from os import listdir  # s4
from termcolor import cprint, colored  # s3

# s2
story_container = ""
with open("./story/story.txt") as story_f:
    for line in story_f:
        story_container += line
story_list = story_container.split("+")

choices = []
with open("./story/choices.txt") as choices_f:
    for line in choices_f:
        choices.append(line.strip())


def warning_unknown_input():  # s1
    """Shows a warning message when the user enters an unknown input"""
    cprint("Unknown input! Please enter a valid one.", "red")


class Game:  # s2
    """
    The game state to be saved when the user passes one level.

    ***

    Attributes:

    char_att_dict: dictionary that stores 'name', 'species', 'gender' keys and values.

    inventory_dict: dictionary that stores 'snack', 'weapon', 'tool' keys and values. New keys pairs can be added.

    difficulty: str to store either 'Easy', 'Medium' or 'Hard'.

    lives: int to store live counts according to the difficulty. 'Easy':5, 'Medium':3, 'Hard':1.

    level: int to store levels of the game. Starts from 1.

    isAlive: bool to store whether the char is alive or not.

    save_file_path: absolute file path.
    """
    char_att_dict = {}
    inventory_dict = {}
    difficulty = "Medium"
    lives = 3
    level = 1
    isAlive = True
    save_file_path = None


class NewGame:  # s2
    """
    A class to use when creating a new game.

    ***

    Attributes:

    char_att_list, char_dict_keys: defaults to create the char_att_dict.

    inventory_list, inventory_dict_keys: defaults to create the inventory_dict.

    username_input: name of the save file for the user.

    ***

    Methods:

    create_new_game: Fills in the Game class attribute values.

    """
    char_att_list = ["1- Name => ", "2- Species => ", "3- Gender => "]
    inventory_list = ["1- Favourite Snack => ", "2- A weapon for the journey => ", "3- A traversal tool => "]
    char_dict_keys = ["name", "species", "gender"]
    inventory_dict_keys = ["snack", "weapon", "tool"]

    def __init__(self, username_input):
        self.username_input = username_input

    def create_new_game(self):  # s2
        """
        Creates a new game by assigning the necessary game state vars.

        ***

        Assigns the save_file_path with an input.

        Assigns the key pairs for Game.char_att_dict.

        Assigns the key pairs for Game.inventory_dict.

        Assigns the difficulty and live attributes in the Game.
        """
        Game.save_file_path = f"./gameSaves/{self.username_input}.txt"

        cprint("Create your character:", "yellow", attrs=["bold", "underline"])

        for i in range(len(self.char_att_list)):
            user_input = input(colored(self.char_att_list[i], "magenta", attrs=["bold"])).title()
            Game.char_att_dict[self.char_dict_keys[i]] = user_input  # save the inputs to a dict

        cprint("Pack your bag for the journey:", "yellow", attrs=["bold", "underline"])

        for j in range(len(self.inventory_list)):
            user_input = input(colored(self.inventory_list[j], "magenta", attrs=["bold"])).title()
            Game.inventory_dict[self.inventory_dict_keys[j]] = user_input

        cprint("Choose your difficulty:", "yellow", attrs=["bold", "underline"])
        cprint("1- Easy\n2- Medium\n3- Hard", "magenta", attrs=["bold"])

        while True:
            difficulty_input = input(colored("=> ", "green", attrs=["bold"]))
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

        cprint("Good luck on your journey " + colored(Game.char_att_dict["name"], "cyan") + "\n", "yellow",
               attrs=["bold"])


class Helper:  # s2
    """Static class that has all the necessary helper methods."""

    @staticmethod
    def increase_lives():
        """Increases the Game.lives count by 1."""
        Game.lives += 1
        print(colored("You gained an extra life! Life count: ", "green", attrs=["bold"]), Game.lives)

    @staticmethod
    def decrease_lives():
        """Decreases the Game.lives count by 1 and sets the Game.isAlive to False."""
        Game.lives -= 1
        Game.isAlive = False
        print(colored("You died! Life count: ", "red", attrs=["bold"]), Game.lives)

    @staticmethod
    def show_inventory():
        """Joins the values of Game.inventory_dict and prints them."""
        inventory = ", ".join(list(Game.inventory_dict.values()))
        cprint(f"Inventory: {inventory}", "cyan")

    @staticmethod
    def add_item(item):
        """
        Adds a key pair to the Game.inventory_dict.

        item:param -> name of the key and value to be added.
        """
        Game.inventory_dict[item] = item

    @staticmethod
    def remove_item(item):
        """
        Removes a key pair from the Game.inventory_dict.

        item:param -> name of the key to be removed.
        """
        Game.inventory_dict.pop(item)

    @staticmethod
    def show_char():
        """Joins the Game.char_att_dict values and Game.lives and prints them."""
        char = ", ".join(list(Game.char_att_dict.values()))
        lives = Game.lives
        cprint(f"Your character: {char}.\nLife count: {lives}", "cyan")

    @staticmethod
    def show_help():
        """Prints the helper commands."""
        cprint("Type the number of the option you want to choose.\n" +
               "Commands you can use:\n/i => Shows inventory.\n" +
               "/q => Exits the game.\n" +
               "/c => Shows character traits.\n" +
               "/h => Shows help.", "blue")

    @staticmethod
    def load_inventory():
        """Reads the save file to store the possible lost items in inventory_dict."""
        with open(Game.save_file_path, "r") as f:
            content = f.readlines()
            inventory = content[1].strip().split(",")

            for i in range(len(inventory)):
                Game.inventory_dict[NewGame.inventory_dict_keys[i]] = inventory[i]

    @staticmethod
    def save_game():  # s4
        """Writes the inventory, character, difficulty, lives to user's file."""
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
                 func1=None, param1=None, func2=None, param2=None, func3=None, param3=None):  # s3
        """
        The core gameplay of the game.

        ***

        story:param -> setting of the current context.

        choice1:param -> first option for the user to choose.

        choice2:param -> second option for the user to choose.

        choice3:param -> third option for the user to choose.

        outcome1:param -> outcome of the first option.

        outcome2:param -> outcome of the second option.

        outcome3:param -> outcome of the third option.

        func1:param -> optional function to return. E.g: Helper.add_item

        param1:param -> optional argument for the first function.

        ...

        PSi: The parameter functions are to be invoked within the gameplay method. So, it shouldn't be invoked
        immediately. Also, the reason for giving the argument for these functions separately is the same as
        pre-mentioned factor.

        PSii: When one wants to move to another setting, pass a print function without calling it. If one don't
        want to move to another setting don't pass any function and remain in the loop.

        """
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


class Levels:  # s3
    """Implements the gameplay on different levels."""

    @staticmethod
    def core_game_loop():
        """Contains the core game loop of the game and invokes the functions according to the level."""
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
        """The gameplay for the first level. Breaks the loop if the char isn't alive."""
        while True:
            cprint("Day 1", "yellow", attrs=["bold", "underline"])
            Game.isAlive = True

            Helper.gameplay(story_list[0], choices[0], choices[1], choices[2],  # s3
                            "\nYou found a key.",
                            f"You used the {Game.inventory_dict['tool']} to go up a bit.",
                            "You admired the majestic view of the mountain!", Helper.add_item, "key", print)

            Helper.gameplay(story_list[1], choices[3], choices[4], choices[5],  # s3
                            "You tried the key on the lock and the door opened." if "key" in Game.inventory_dict
                            else "You don't have a key to open the lock.",
                            """The bird has red wings with blue stripes on. It has a long neck.
Inside its beak it has sharp teeth and its eyes are following you, interested.""",
                            f"""You take out your {Game.inventory_dict['weapon']} and attack the bird.
It stretches its head to attack you. It's too fast...""", Helper.remove_item if "key" in Game.inventory_dict
                            else None, "key", func3=Helper.decrease_lives)
            if not Game.isAlive:
                break

            Helper.gameplay(story_list[2], choices[6], choices[7], choices[8],
                            """The voice says 'Too bad, I thought you were clever!' as it gets closer to you. 
You see a shape like gorilla for a second and you can't even make a peep...""",
                            "The darkness says 'Wrong!'. You try to run but it catches you from your legs and drags you to darkness...",
                            """The darkness says 'Correct! You may pass traveller.'
You saw a light coming from the inner cave and you follow it.""",
                            Helper.decrease_lives, func2=Helper.decrease_lives,
                            func3=Helper.save_game)
            if not Game.isAlive:
                break

            if Game.level == 2:
                break

    @staticmethod
    def level2():
        """The gameplay for the second level. Breaks the loop if the char isn't alive."""
        while True:
            Helper.load_inventory()
            cprint("Day 2", "yellow", attrs=["bold", "underline"])
            Game.isAlive = True

            Helper.gameplay(story_list[3], choices[9], f"{choices[10]} {Game.inventory_dict['weapon']}.", choices[11],
                            f"""The dragon smacks its lips and shows its tongue. 
It looks hungry, you remember you have {Game.inventory_dict['snack'] if 'snack' in Game.inventory_dict else "no snack."}.""",
                            "\n***You get closer to the dragon slowly and with one swift blow, it's dead.",
f"""You take out {Game.inventory_dict['snack'] if 'snack' in Game.inventory_dict else "no snack."} from your bag and give it to the dragon.
The dragon loves it and flies away happily.""", func2=print, func3=Helper.remove_item, param3="snack")

            Helper.gameplay(story_list[4], choices[12], choices[13], choices[14],
                            "You open the chest on the left. You found an extra life!", """You open the chest on the right but the chest is empty.
You try to look inside closely but something pushes you inside the chest.
The chest close itself.""", "The hood disappears without a trace as you walk away from it.",
                            Helper.increase_lives, func2=Helper.decrease_lives, func3=print)
            if not Game.isAlive:
                break

            Helper.gameplay(story_list[5], choices[15], f"{choices[16]} {Game.inventory_dict['weapon']}", choices[17],
                            "The dragon shoots flame to your way and burn you!",
                            "The dragon crushes you with its tail, you don't even see it coming...",
                            """The smaller dragon from before appear behind the mother and flies to you, showing affection for you.
You pet its head and the mother dragon looks happy about this.
Congratulations! You've conquered the mountain!""" if 'snack' not in Game.inventory_dict else
                            "Nothing happens. The dragon moves its wings and the wind knocks you off from the mountain...",
                            Helper.decrease_lives, func2=Helper.decrease_lives,
                            func3=exit if 'snack' not in Game.inventory_dict else Helper.decrease_lives)
            if not Game.isAlive:
                break


class Menu:  # s1, in the s1 ,the functions should be passed, they are implemeted in s2
    """Menu class to print the options and welcome message."""
    options = """
    
1- Press key '1' or type 'start' to start a new game
2- Press key '2' or type 'load' to load your progress
3- Press key '3' or type 'quit' to quit the game"""

    def __init__(self, user_input):
        self.user_input = user_input

    @staticmethod
    def welcome():
        """Prints the welcome message and the title of the game."""
        title = "Journey to Mount Qaf"
        print(colored(f"\n***Welcome to the {title}***", "yellow", attrs=["bold"]),
              colored(Menu.options, "magenta", attrs=["bold"]))

    def new_game(self):
        """Invokes the NewGame.create_new_game and Levels.core_game_loop functions."""
        cprint("Starting a new game...", "blue")  # s1
        message = colored("Enter a user name to save your progress or type '/b' to go back => ", "magenta",
                          attrs=["bold"])  # s2
        new_game = NewGame(input(message))
        while True:
            if new_game.username_input == "/b":
                cprint("Going back to menu...", "blue")
                break
            else:
                new_game.create_new_game()
                Levels.core_game_loop()
            break  # go back to menu

    def load_game(self):
        """Checks to see if a save file exist and reads the file content to assign the Game class attributes."""
        try:  # s4
            saves = list(map(lambda x: x.replace(".txt", ""), listdir('./gameSaves/')))  # get rid of .txt
            cprint("Type your username from the list:", "yellow")
            for save in saves:
                cprint(save, "magenta", attrs=["bold"])
            path = input(colored("=> ", "green", attrs=["bold"]))
            Game.save_file_path = f'./gameSaves/{path}.txt'
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


# s1
game_menu = Menu(None)

while True:  # s1
    Menu.welcome()

    game_menu.user_input = input(colored("=> ", "green", attrs=["bold"]))

    if game_menu.user_input == "1" or game_menu.user_input.lower() == "start":
        game_menu.new_game()

    elif game_menu.user_input == "2" or game_menu.user_input.lower() == "load":
        game_menu.load_game()

    elif game_menu.user_input == "3" or game_menu.user_input.lower() == "quit":
        cprint("Goodbye!", "blue")
        break

    else:
        warning_unknown_input()
