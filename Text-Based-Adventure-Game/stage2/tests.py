from typing import Any
from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult


class TextBasedAdventureGameTest(StageTest):
    username = "new_user"
    name = "john"
    species = "human"
    gender = "male"
    snack = "apple"
    weapon = "sword"
    tool = "rope"
    difficulty = "easy"

    def generate(self) -> [TestCase]:
        return [
            TestCase(stdin=[self.check_welcome]),
            TestCase(stdin=["1", self.check_start_load]),
            TestCase(stdin=["start", self.check_start_load]),
            TestCase(stdin=["StARt", self.check_start_load]),
            TestCase(stdin=["2", self.check_start_load]),
            TestCase(stdin=["load", self.check_start_load]),
            TestCase(stdin=["lOAd", self.check_start_load]),
            TestCase(stdin=["5", self.check_unknown]),
            TestCase(stdin=["1", self.check_username, self.name, self.species, self.gender, self.snack, self.weapon,
                            self.tool, self.difficulty, self.check_game_state, "3"]),
            TestCase(stdin=["1", "/b", self.check_go_back]),
            TestCase(stdin="3"),
            TestCase(stdin="quIt")
        ]

    def check_welcome(self, output):
        if "welcome to" not in output.lower() and "***" not in output:
            return CheckResult.wrong("You didn't output a correct welcome message!")
        return CheckResult.correct()

    def check_start_load(self, output):
        if "starting a new game" in output.lower() or "no save data found" in output.lower():
            return CheckResult.correct()
        return CheckResult.wrong("Your program didn't output correct message.")

    def check_unknown(self, output):
        if "unknown input! please enter a valid one" in output.lower():
            return "3"
        return CheckResult.wrong("Your program couldn't process unknown input.")

    def check_username(self, output):
        if "enter a username" not in output.lower() and "/b" not in output.lower():
            return CheckResult.wrong("You didn't ask for the username and didn't give the option to go back.")
        return self.username

    def check_game_state(self, output):
        states = [self.name, self.species, self.gender, self.snack, self.weapon, self.tool, self.difficulty]
        have_state = all([state in output.lower() for state in states])
        if "good luck on your journey" not in output.lower():
            return CheckResult.wrong("You didn't output the correct message.")
        elif not have_state:
            return CheckResult.wrong("You didn't output the correct game state.")
        return CheckResult.correct()

    def check_go_back(self, output):
        if "going back to menu" not in output.lower():
            CheckResult.wrong("You didn't output the correct message when going back to menu.")
        return "3"

    def check(self, reply: str, attach: Any) -> CheckResult:
        if "goodbye!" in reply.lower():
            return CheckResult.correct()
        return CheckResult.wrong("Your program didn't print a correct goodbye message.")


if __name__ == '__main__':
    TextBasedAdventureGameTest('game.game').run_tests()
