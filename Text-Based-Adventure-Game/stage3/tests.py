from typing import Any
from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult
from random import choice


class TextBasedAdventureGameTest(StageTest):
    username = "new_user01"
    name = "john"
    species = "human"
    gender = "male"
    snack = "apple"
    weapon = "sword"
    tool = "rope"
    difficulty = "easy"
    lives = "5"
    choices = ["1", "2", "3"]
    player_choice = choice(choices)

    def generate(self) -> [TestCase]:
        return [
            TestCase(stdin=[self.check_welcome]),
            TestCase(stdin=["1", self.check_start_load]),
            TestCase(stdin=["start", self.check_start_load]),
            TestCase(stdin=["StARt", self.check_start_load]),
            TestCase(stdin=["2", self.check_start_load]),
            TestCase(stdin=["load", self.check_start_load]),
            TestCase(stdin=["lOAd", self.check_start_load]),
            TestCase(stdin=["4", self.check_unknown]),
            TestCase(stdin=["1", self.check_username, self.name, self.species, self.gender, self.snack, self.weapon,
                            self.tool, self.difficulty, self.check_game_state, "3"]),
            TestCase(stdin=["1", "/b", self.check_go_back]),
            TestCase(stdin=["1", self.check_username, self.name, self.species, self.gender, self.snack, self.weapon,
                            self.tool, self.difficulty, self.player_choice, (-1, self.check_gameplay)]),
            TestCase(stdin=["1", self.check_username, self.name, self.species, self.gender, self.snack, self.weapon,
                            self.tool, self.difficulty, "/i", self.check_inventory]),
            TestCase(stdin=["1", self.check_username, self.name, self.species, self.gender, self.snack, self.weapon,
                            self.tool, self.difficulty, "/c", self.check_char]),
            TestCase(stdin=["1", self.check_username, self.name, self.species, self.gender, self.snack, self.weapon,
                            self.tool, self.difficulty, "/h", self.check_help]),
            TestCase(stdin=["1", self.check_username, self.name, self.species, self.gender, self.snack, self.weapon,
                            self.tool, self.difficulty, "/q", (2, self.check_quit)]),
            TestCase(stdin=["1", self.check_username, self.name, self.species, self.gender, self.snack, self.weapon,
                            self.tool, self.difficulty, "4", self.check_unknown]),
            TestCase(stdin="3"),
            TestCase(stdin="quIt")
        ]

    def check_welcome(self, output):
        if "welcome to" not in output.lower() and "***" not in output:
            return CheckResult.wrong("You didn't output a correct welcome message!")
        return CheckResult.correct()

    def check_start_load(self, output):
        if "starting a new game..." in output.lower() or "loading your progress..." in output.lower():
            return CheckResult.correct()
        return CheckResult.wrong("Your program didn't output correct message.")

    def check_unknown(self, output):
        if "unknown input! please enter a valid one." in output.lower():
            return CheckResult.correct()
        return CheckResult.wrong("Your program couldn't process unknown input.")

    def check_username(self, output):
        if "enter a username" not in output.lower() and "/b" not in output.lower():
            return CheckResult.wrong("You didn't ask for the username and didn't give the option to go back.")
        return self.username

    def check_game_state(self, output):
        states = [self.name, self.species, self.gender, self.snack, self.weapon, self.tool, self.difficulty]
        have_state = all([state in output.lower() for state in states])
        if "good luck on your journey:" not in output.lower():
            return CheckResult.wrong("You didn't output the correct message.")
        elif not have_state:
            return CheckResult.wrong("You didn't output the correct game state.")
        return CheckResult.correct()

    def check_go_back(self, output):
        if "going back to menu..." not in output.lower():
            CheckResult.wrong("You didn't output the correct message when going back to menu.")
        return "3"

    def check_gameplay(self, output):
        choices = self.choices.copy()
        if "level 2" in output.lower() or "game over" in output.lower():
            return CheckResult.correct()

        if "you died" in output.lower() and "level 1" not in output.lower():
            return CheckResult.wrong("Your program didn't start from the beginning of the level")

        if "what will you do? type the number of the option or type '/h' to show help." not in output.lower():
            choices.pop(choices.index(self.player_choice))
            random_choice = choice(choices)
            self.player_choice = random_choice
            return random_choice

        else:
            random_choice = choice(choices)
            self.player_choice = random_choice
            return random_choice

    def check_inventory(self, output):
        inventory = [self.snack, self.weapon, self.tool]
        in_inventory = all([item in output.lower() for item in inventory])

        if "inventory" not in output.lower() or not in_inventory:
            return CheckResult.wrong("Your program didn't output correct inventory content.")
        else:
            return CheckResult.correct()

    def check_char(self, output):
        char = [self.name, self.species, self.gender, self.lives]
        in_char = all([ch in output.lower() for ch in char])
        if "character" not in output.lower() or not in_char or "life count" not in output.lower():
            return CheckResult.wrong("Your program didn't output correct character traits.")
        else:
            return CheckResult.correct()

    def check_help(self, output):
        message = "type the number of the option you want to choose.\n" + "commands you can use:\n/i => shows inventory.\n" \
                  + "/q => exits the game.\n" + "/c => shows character traits.\n" + "/h => shows help."
        if message not in output.lower():
            return CheckResult.wrong("Your program didn't output the correct help message.")
        else:
            return CheckResult.correct()

    def check_quit(self, output):
        if "you sure you want to quit the game? y/n " in output.lower():
            return "y"
        elif "goodbye!" in output.lower():
            return CheckResult.correct()
        else:
            return CheckResult.wrong("You didn't ask to quit the game.")





    def check(self, reply: str, attach: Any) -> CheckResult:
        if "goodbye!" in reply.lower():
            return CheckResult.correct()
        return CheckResult.wrong("Your program didn't print a correct goodbye message.")


if __name__ == '__main__':
    TextBasedAdventureGameTest('txt-based-adv-game.game').run_tests()
