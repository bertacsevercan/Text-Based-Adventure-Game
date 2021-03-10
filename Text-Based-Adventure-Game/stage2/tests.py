from hstest import StageTest, CheckResult, dynamic_test, TestedProgram


class TextBasedAdventureGameTest(StageTest):
    username = "new_user"
    name = "john"
    species = "human"
    gender = "male"
    snack = "apple"
    weapon = "sword"
    tool = "rope"
    difficulty = "easy"
    lives = 5

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
            feedback = "Your program couldn't process input '1' to start a new game! Make sure to output 'Starting a new game...'."
            return self.check_start_new(output, feedback)
        return CheckResult.wrong("Your program didn't ask for input!")

    @dynamic_test
    def test3(self):
        main = TestedProgram()
        main.start()

        if main.is_waiting_input():
            output = main.execute("start")
            feedback = "Your program couldn't process the input 'start' to start a new game! Make sure to output 'Starting a new game...'."
            return self.check_start_new(output, feedback)
        return CheckResult.wrong("Your program didn't ask for input!")

    @dynamic_test
    def test4(self):
        main = TestedProgram()
        main.start()

        if main.is_waiting_input():
            output = main.execute("StARt")
            feedback = "Your program shouldn't be case sensitive when starting a new game!"
            return self.check_start_new(output, feedback)
        return CheckResult.wrong("Your program didn't ask for input!")

    @dynamic_test
    def test5(self):
        main = TestedProgram()
        main.start()

        if main.is_waiting_input():
            output = main.execute("2")
            feedback = "Your program couldn't process input '2' to load a game! Make sure to say 'No save data found!'."
            return self.check_start_load(output, feedback)
        return CheckResult.wrong("Your program didn't ask for input!")

    @dynamic_test
    def test6(self):
        main = TestedProgram()
        main.start()

        if main.is_waiting_input():
            output = main.execute("load")
            feedback = "Your program couldn't process input 'load' to load a game! Make sure to say 'No save data found!'."
            return self.check_start_load(output, feedback)
        return CheckResult.wrong("Your program didn't ask for input!")

    @dynamic_test
    def test7(self):
        main = TestedProgram()
        main.start()

        if main.is_waiting_input():
            output = main.execute("lOAd")
            feedback = "Your program shouldn't be case sensitive when loading a game!."
            return self.check_start_load(output, feedback)
        return CheckResult.wrong("Your program didn't ask for input!")

    @dynamic_test
    def test8(self):
        main = TestedProgram()
        main.start()

        if main.is_waiting_input():
            output = main.execute("5")
            if main.is_waiting_input():
                return self.check_unknown(output)
            return CheckResult.wrong("Your program didn't ask for another input after an unknown input!")
        return CheckResult.wrong("Your program didn't ask for input!")

    @dynamic_test
    def test9(self):
        main = TestedProgram()
        main.start()

        if main.is_waiting_input():
            output = main.execute("3")
            if main.is_finished():
                feedback = "Your program didn't output 'Goodbye!' before you exit with '3' as input!"
                return self.check_quit(output, feedback)
            return CheckResult.wrong("Your program should end with input '3'!")
        return CheckResult.wrong("Your program didn't ask for input!")

    @dynamic_test
    def test10(self):
        main = TestedProgram()
        main.start()

        if main.is_waiting_input():
            output = main.execute("quIt")
            if main.is_finished():
                feedback = "Your program didn't output 'Goodbye!' before you exit with 'quIt' as input! Your program must be case insensitive!"
                return self.check_quit(output, feedback)
            return CheckResult.wrong(
                "Your program should end with input 'quIt'! Your program must be case insensitive!")
        return CheckResult.wrong("Your program didn't ask for input!")

    @dynamic_test
    def test11(self):
        main = TestedProgram()
        main.start()

        if main.is_waiting_input():
            output = main.execute("quit")
            if main.is_finished():
                feedback = "Your program didn't output 'Goodbye!' before you exit with 'quit' as input!"
                return self.check_quit(output, feedback)
            return CheckResult.wrong("Your program should end with input 'quit'!")
        return CheckResult.wrong("Your program didn't ask for input!")

    @dynamic_test
    def test12(self):
        main = TestedProgram()
        main.start()
        output1 = main.execute("1")

        if "/b" not in output1.lower():
            return CheckResult.wrong("Show the user that they can enter '/b' to go back!")
        elif "enter a user name" not in output1.lower():
            return CheckResult.wrong("Tell the user to 'Enter a user name'!")

        if main.is_waiting_input():
            output2 = main.execute("/b").lower()

            if "create your character" in output2:
                return CheckResult.wrong(
                    "You didn't process the right command for going back which is '/b'!")

            if "going back to menu" not in output2:
                return CheckResult.wrong(
                    "You didn't output the correct message when going back to menu. Make sure the output contains 'Going back to menu...'")

            if not main.is_waiting_input():
                return CheckResult.wrong("Your program should continue working in the main menu")

            return self.check_welcome(output2, feedback="You should output the same welcome message with the menu!")

        return CheckResult.wrong("Your program didn't ask for input!")

    def check_welcome(self, output, feedback=""):
        if "welcome to" in output.lower() and "***" in output:
            return CheckResult.correct()
        return CheckResult.wrong(
            feedback or "Your welcome message doesn't include the following: ***Welcome to <game-title>***' !")

    def check_start_new(self, output, feedback):
        if "starting a new game" in output.lower():
            return CheckResult.correct()
        return CheckResult.wrong(feedback)

    def check_start_load(self, output, feedback):
        if "no save data found" in output.lower():
            return CheckResult.correct()
        return CheckResult.wrong(feedback)

    def check_unknown(self, output):
        if "unknown input! please enter a valid one" in output.lower():
            return CheckResult.correct()
        return CheckResult.wrong(
            "Your program couldn't process unknown input. Make sure to say 'Unknown input! Please enter a valid one'. ")

    def check_quit(self, output, feedback):
        if "goodbye" in output.lower():
            return CheckResult.correct()
        return CheckResult.wrong(feedback)

    # def check_go_back(self, output):
    #     if "going back to menu" in output.lower():
    #         return CheckResult.correct()
    #     return CheckResult.wrong(
    #         "You didn't output the correct message when going back to menu. Make sure the output contains 'going back to menu'")

    # def generate(self) -> [TestCase]:
    #     return [
    #         TestCase(stdin=[self.check_welcome]),
    #         TestCase(stdin=["1", self.check_start_load]),
    #         TestCase(stdin=["start", self.check_start_load]),
    #         TestCase(stdin=["StARt", self.check_start_load]),
    #         TestCase(stdin=["2", self.check_start_load]),
    #         TestCase(stdin=["load", self.check_start_load]),
    #         TestCase(stdin=["lOAd", self.check_start_load]),
    #         TestCase(stdin=["5", self.check_unknown]),
    #         TestCase(stdin=["1", self.check_username, self.name, self.species, self.gender, self.snack, self.weapon,
    #                         self.tool, self.difficulty, self.check_game_state, "3"]),
    #         TestCase(stdin=["1", "/b", self.check_go_back]),
    #         TestCase(stdin="3"),
    #         TestCase(stdin="quIt")
    #     ]
    #
    # def check_welcome(self, output):
    #     if "welcome to" not in output.lower() and "***" not in output:
    #         return CheckResult.wrong("You didn't output a correct welcome message!")
    #     return CheckResult.correct()
    #
    # def check_start_load(self, output):
    #     if "starting a new game" in output.lower() or "no save data found" in output.lower():
    #         return CheckResult.correct()
    #     return CheckResult.wrong("Your program didn't output correct message.")
    #
    # def check_unknown(self, output):
    #     if "unknown input! please enter a valid one" in output.lower():
    #         return "3"
    #     return CheckResult.wrong("Your program couldn't process unknown input.")
    #
    # def check_username(self, output):
    #     if "enter a username" not in output.lower() and "/b" not in output.lower():
    #         return CheckResult.wrong("You didn't ask for the username and didn't give the option to go back.")
    #     return self.username
    #
    # def check_game_state(self, output):
    #     states = [self.name, self.species, self.gender, self.snack, self.weapon, self.tool, self.difficulty]
    #     have_state = all([state in output.lower() for state in states])
    #     if "good luck on your journey" not in output.lower():
    #         return CheckResult.wrong("You didn't output the correct message.")
    #     elif not have_state:
    #         return CheckResult.wrong("You didn't output the correct game state.")
    #     return CheckResult.correct()
    #
    # def check_go_back(self, output):
    #     if "going back to menu" not in output.lower():
    #         CheckResult.wrong("You didn't output the correct message when going back to menu.")
    #     return "3"
    #
    # def check(self, reply: str, attach: Any) -> CheckResult:
    #     if "goodbye!" in reply.lower():
    #         return CheckResult.correct()
    #     return CheckResult.wrong("Your program didn't print a correct goodbye message.")


if __name__ == '__main__':
    TextBasedAdventureGameTest('game.game').run_tests()
