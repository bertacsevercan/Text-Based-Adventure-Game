from typing import Any
from hstest.stage_test import StageTest
from hstest.test_case import TestCase
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
        if "welcome to" not in output.lower() and "***" not in output:
            return CheckResult.wrong("You didn't output a correct welcome message!")
        return CheckResult.correct()

    def check_start_load(self, output):
        if "starting a new game" in output.lower() or "no save data found" in output.lower():
            return CheckResult.correct()
        return CheckResult.wrong("Your program didn't output correct message.")

    def check_unknown(self, output):
        if "unknown input! please enter a valid one." in output.lower():
            return "3"
        return CheckResult.wrong("Your program couldn't process unknown input.")

    def check(self, reply: str, attach: Any) -> CheckResult:
        if "goodbye!" in reply.lower():
            return CheckResult.correct()

        return CheckResult.wrong("Your program didn't print a correct goodbye message.")


if __name__ == '__main__':
    TextBasedAdventureGameTest('game.game').run_tests()
