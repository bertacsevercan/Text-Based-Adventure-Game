from typing import Any
from hstest.stage_test import StageTest, TestPassed, WrongAnswer
from hstest.test_case import TestCase, SimpleTestCase
from hstest.check_result import CheckResult


class TextBasedAdventureGameTest(StageTest):
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
            TestCase(stdin="3"),
            TestCase(stdin="quIt")
        ]

    def check_welcome(self, output):
        if "Welcome to" not in output and "***" not in output:
            return CheckResult.wrong("You didn't output a correct welcome message!")
        return CheckResult.correct()

    def check_start_load(self, output):
        if "Starting a new game..." in output or "Loading your progress..." in output:
            return CheckResult.correct()
        return CheckResult.wrong("Your program didn't output correct message.")

    def check_exit(self, output):
        if "Goodbye!" in output:
            raise TestPassed()
        else:
            raise WrongAnswer("Your program didn't print a goodbye message.")

    def check_unknown(self, output):
        if "Unknown input! Please enter a valid one." in output:
            return "3"
        return CheckResult.wrong("Your program couldn't process unknown input.")

    def check(self, reply: str, attach: Any) -> CheckResult:
        if "Goodbye!" in reply:
            return CheckResult.correct()

        return CheckResult.wrong("Your program didn't print a correct goodbye message.")


if __name__ == '__main__':
    TextBasedAdventureGameTest('txt-based-adv-game.game').run_tests()
