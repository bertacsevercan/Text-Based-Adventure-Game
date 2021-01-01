from sys import exit  # s1
from os import listdir  # s4

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
    isAlive = True


class NewGame:  # s2
    char_att_list = ["1- Name => ", "2- Species => ", "3- Gender => "]
    inventory_list = ["1- Favourite Snack => ", "2- A weapon for the journey => ", "3- A traversal tool => "]
    char_dict_keys = ["name", "species", "gender"]
    inventory_dict_keys = ["snack", "weapon", "tool"]
    save_file_path = None

    def __init__(self, username_input):
        self.username_input = username_input

    def create_new_game(self):  # s2
        NewGame.save_file_path = f"./gameSaves/{self.username_input}.txt"

        print("Create your character:")

        for i in range(len(self.char_att_list)):
            user_input = input(self.char_att_list[i]).title()
            Game.char_att_dict[self.char_dict_keys[i]] = user_input  # save the inputs to a dict

        print("Pack your bag for the journey:")

        for j in range(len(self.inventory_list)):
            user_input = input(self.inventory_list[j]).title()
            Game.inventory_dict[self.inventory_dict_keys[j]] = user_input

        print("""Choose your difficulty:
1- Easy
2- Medium
3- Hard""")
        while True:
            difficulty_input = input("=> ")
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

        print("Good luck on your journey " + Game.char_att_dict["name"] + "!\n")


class Helper:  # s2

    @staticmethod
    def increase_lives():
        Game.lives += 1
        print("You gained an extra life! Life count: ", Game.lives)

    @staticmethod
    def decrease_lives():
        Game.lives -= 1
        Game.isAlive = False
        print("You died! Life count: ", Game.lives)

    @staticmethod
    def show_inventory():
        inventory = ", ".join(list(Game.inventory_dict.values()))
        print(f"Inventory: {inventory}")

    @staticmethod
    def add_item(item):
        Game.inventory_dict[item] = item

    @staticmethod
    def remove_item(item):
        Game.inventory_dict.pop(item)

    @staticmethod
    def save_game():  # s4
        print("You've found a safe spot to rest. Saving your progress...")
        inventory = ", ".join(list(Game.inventory_dict.values()))
        char_atts = ", ".join(list(Game.char_att_dict.values()))
        Game.level += 1
        with open(NewGame.save_file_path, "w") as f:
            writings = [char_atts + "\n", inventory + "\n", str(Game.difficulty) + " ", str(Game.lives) + "\n",
                        str(Game.level) + "\n"]
            f.writelines(writings)

    @staticmethod
    def gameplay(story, choice1, choice2, choice3, outcome1, outcome2, outcome3,
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
                if func1 is not None:
                    if param1 is None:
                        return func1()
                    return func1(param1)
                else:
                    continue
            elif action_input == "2":
                print(outcome2)
                if func2 is not None:
                    if param2 is None:
                        return func2()
                    return func2(param2)
                else:
                    continue
            elif action_input == "3":
                print(outcome3)
                if func3 is not None:
                    if param3 is None:
                        return func3()
                    return func3(param3)
                else:
                    continue
            elif action_input.lower() == "/i":
                Helper.show_inventory()
            elif action_input.lower() == "/q":
                message = "You sure you want to quit the game? Y/N => "
                exit_input = input(message)
                if exit_input.lower() == "y":
                    print("Goodbye!")
                    exit()
                else:
                    continue
            else:
                warning_unknown_input()


class Levels:  # s3

    @staticmethod
    def core_game(level):
        while True:
            if Game.lives > 0:
                if level == 1:
                    Levels.level1()
                elif level == 2:
                    Levels.level2()
                else:
                    print("Oops! Something went wrong.")
                    break
            else:
                print("You ran out of lives! Game over!")
                break

    @staticmethod
    def level1():
        while True:
            print("Day 1")
            Game.isAlive = True

            Helper.gameplay(story_list[0], choices[0], choices[1], choices[2],  # s3
                            "You found a key.",
                            f"You used the {Game.inventory_dict['tool']} to go up a bit.",
                            "You admired the majestic view of the mountain!", Helper.add_item, "key", print)

            Helper.gameplay(story_list[1], choices[3], choices[4], choices[5],  # s3
                            "You tried the key on the lock and the door opened." if "key" in Game.inventory_dict
                            else "You don't have a key to open the lock.",
                            """The bird has red wings with blue stripes on. It has a long neck.
Inside its beak it has sharp teeth and its eyes are following you, interested.""",
                            f"""You take out your {Game.inventory_dict['weapon']} and attack the bird.
It stretches its head and chops your head off.""", Helper.remove_item if "key" in Game.inventory_dict
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

    @staticmethod
    def level2():
        print("Day 2")

        Helper.gameplay(story_list[3], choices[9], f"{choices[10]} {Game.inventory_dict['weapon']}.", choices[11],
                        f"""The dragon smacks its lips and shows its tongue. 
It looks hungry, you remember you have {Game.inventory_dict['snack'] if 'snack' in Game.inventory_dict else "no snack."}.""",
                        "You get closer to the dragon slowly and with one swift blow, it's dead.",
                        f"""You take out {Game.inventory_dict['snack'] if 'snack' in Game.inventory_dict else "no snack."} from your bag and give it to the dragon.
The dragon loves it and flies away happily.""", func2=print, func3=Helper.remove_item, param3="snack")

        Helper.gameplay(story_list[4], choices[12], choices[13], choices[14],
                        "You open the chest on the left. You found an extra life!", """You open the chest on the right but the chest is empty.
You try to look inside closely but something pushes you inside the chest.
The chest close itself.""", "The hood disappears without a trace as you walk away from it.",
                        Helper.increase_lives, func2=Helper.decrease_lives, func3=print)
        Helper.gameplay(story_list[5], choices[15], f"{choices[16]} {Game.inventory_dict['weapon']}", choices[17],
                        "The dragon shoots flame to your way and burn you!",
                        "The dragon crushes you with its tail, you don't even see it coming...",
                        """The smaller dragon from before appear behind the mother and flies to you, showing affection for you.
                        You pet its head and the mother dragon looks happy about this.
                        Congratulations! You've conquered the mountain!""" if 'snack' not in Game.inventory_dict else
                        "Nothing happens. The dragon moves its wings and the wind knocks you off from the mountain...",
                        Helper.decrease_lives, func2=Helper.decrease_lives,
                        func3=exit if 'snack' not in Game.inventory_dict else Helper.decrease_lives)


class Menu:  # s1, in the s1 ,the functions should be passed, they are implemeted in s2

    options = """
    
1- Press key '1' or type 'start' to start a new game
2- Press key '2' or type 'load' to load your progress
3- Press key '3' or type 'quit' to quit the game"""

    def __init__(self, user_input):
        self.user_input = user_input

    @staticmethod
    def welcome():
        title = "Journey to Mount Qaf"
        print(f"***Welcome to the {title}***", Menu.options)

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
                Levels.core_game(Game.level)
            break  # go back to menu


def load_game(self):
    print("Loading your progress...")  # s1
    try:  # s4
        path = './gameSaves/' + listdir('./gameSaves/')[0]
        with open(path, "r") as f:
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

            Levels.core_game(Game.level)

    except TypeError:
        print("No save data found!")


# s1
game_menu = Menu(None)

while True:  # s1
    Menu.welcome()

    game_menu.user_input = input("=> ")

    if game_menu.user_input == "1" or game_menu.user_input.lower() == "start":
        game_menu.new_game()

    elif game_menu.user_input == "2" or game_menu.user_input.lower() == "load":
        game_menu.load_game()

    elif game_menu.user_input == "3" or game_menu.user_input.lower() == "quit":
        break

    else:
        warning_unknown_input()
