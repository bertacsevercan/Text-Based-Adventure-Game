from hstest import StageTest, TestCase, CheckResult, dynamic_test, TestedProgram


class TextBasedAdventureGameTest(StageTest):

    @dynamic_test
    def test1(self):
        main = TestedProgram()
        output = main.start()
        return self.check_welcome(output)

    @dynamic_test
    def test2(self):
        main = TestedProgram()
        main.start()

        if main.is_waiting_input():
            output = main.execute("1")
            feedback = "Your program couldn't process input '1' to start a new game! Make sure to output 'starting a new game'."
            return self.check_start_new(output, feedback)
        return CheckResult.wrong("Your program didn't ask for input!")

    @dynamic_test
    def test3(self):
        main = TestedProgram()
        main.start()

        if main.is_waiting_input():
            output = main.execute("StARt")
            feedback = "Your program shouldn't be case sensitive when starting a new game!"
            return self.check_start_new(output, feedback)
        return CheckResult.wrong("Your program didn't ask for input!")

    @dynamic_test
    def test4(self):
        main = TestedProgram()
        main.start()

        if main.is_waiting_input():
            output = main.execute("2")
            feedback = "Your program couldn't process input '2' to load a game! Make sure to say 'no save data found'."
            return self.check_start_load(output, feedback)
        return CheckResult.wrong("Your program didn't ask for input!")

    @dynamic_test
    def test5(self):
        main = TestedProgram()
        main.start()

        if main.is_waiting_input():
            output = main.execute("lOAd")
            feedback = "Your program shouldn't be case sensitive when loading a game!."
            return self.check_start_load(output, feedback)
        return CheckResult.wrong("Your program didn't ask for input!")

    @dynamic_test
    def test6(self):
        main = TestedProgram()
        main.start()

        if main.is_waiting_input():
            output = main.execute("5")
            return self.check_unknown(output)
        return CheckResult.wrong("Your program didn't ask for input!")

    @dynamic_test
    def test7(self):
        main = TestedProgram()
        main.start()

        if main.is_waiting_input():
            output = main.execute("3")
            if main.is_finished():
                feedback = "Your program didn't output 'goodbye' before you exit with '3' as input!"
                return self.check_quit(output, feedback)
            return CheckResult.wrong("Your program should end with input '3'!")
        return CheckResult.wrong("Your program didn't ask for input!")

    @dynamic_test
    def test8(self):
        main = TestedProgram()
        main.start()

        if main.is_waiting_input():
            output = main.execute("quIt")
            if main.is_finished():
                feedback = "Your program didn't output 'goodbye' before you exit with 'quIt' as input! Your program must be case insensitive!"
                return self.check_quit(output, feedback)
            return CheckResult.wrong("Your program should end with input 'quIt'! Your program must be case insensitive!")
        return CheckResult.wrong("Your program didn't ask for input!")


    @dynamic_test
    def test9(self):
        main = TestedProgram()
        main.start()

        if main.is_waiting_input():
            output = main.execute("quit")
            if main.is_finished():
                feedback = "Your program didn't output 'goodbye' before you exit with 'quit' as input!"
                return self.check_quit(output, feedback)
            return CheckResult.wrong("Your program should end with input 'quit'!")
        return CheckResult.wrong("Your program didn't ask for input!")



    # def generate(self) -> [TestCase]:
    #     return [
    #         TestCase(stdin=[self.check_welcome]),
    #         TestCase(stdin=["1", self.check_start_new]),
    #         TestCase(stdin=["StARt", self.check_start_new_letter_case]),
    #         TestCase(stdin=["2", self.check_start_load]),
    #         TestCase(stdin=["lOAd", self.check_start_load_letter_case]),
    #         TestCase(stdin=["5", self.check_unknown]),
    #         # TestCase(stdin=["3", self.check_quit_numbered_input]),
    #         # TestCase(stdin=["quIt", self.check_quit_word_input])
    #     ]

    # @dynamic_test
    # def test(self):
    #     main = TestedProgram()
    #
    #     output = main.start()
    #     output2 = main.execute("3")
    #     return self.check_quit_numbered_input(output2)

    def check_welcome(self, output):
        if "welcome to" in output.lower() and "***" in output:
            return CheckResult.correct()
        return CheckResult.wrong("You welcome message doesn't include the following: 'welcome to', '***' !")

    def check_start_new(self, output, feedback):
        if "starting a new game" in output.lower():
            return CheckResult.correct()
        return CheckResult.wrong(feedback)

    # def check_start_new_letter_case(self, output):
    #     if "starting a new game" in output.lower():
    #         return CheckResult.correct()
    #     return CheckResult.wrong("Your program shouldn't be case sensitive when starting a new game!")

    def check_start_load(self, output, feedback):
        if "no save data found" in output.lower():
            return CheckResult.correct()
        return CheckResult.wrong(feedback)

    # def check_start_load_letter_case(self, output):
    #     if "no save data found" in output.lower():
    #         return CheckResult.correct()
    #     return CheckResult.wrong("Your program shouldn't be case sensitive when loading a game!")

    def check_unknown(self, output):
        if "unknown input! please enter a valid one" in output.lower():
            return CheckResult.correct()  # "3"
        return CheckResult.wrong(
            "Your program couldn't process unknown input. Make sure to say 'unknown input! please enter a valid one'. ")

    def check_quit(self, output, feedback):
        if "goodbye" in output.lower():
            return CheckResult.correct()
        return CheckResult.wrong(feedback)

    # def check_quit_word_input(self, output):
    #     if "goodbye" in output.lower():
    #         return CheckResult.correct()
    #     return CheckResult.wrong(
    #         "Your program shouldn't be case sensitive!")
    #
    # def check(self, reply: str, attach: Any) -> CheckResult:
    #     if "goodbye" in reply.lower():
    #         return CheckResult.correct()
    #     return CheckResult.wrong(
    #         "Your program shouldn't be case sensitive!")


if __name__ == '__main__':
    TextBasedAdventureGameTest('game.game').run_tests()
