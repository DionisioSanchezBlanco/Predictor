class GenerateRandomness:
    """Generate randomness"""

    def __init__(self):
        """Initiate user input"""
        self.number = ''
        self.profile = {"000": [0, 0], "001": [0, 0], "010": [0, 0], "011": [0, 0],
                        "100": [0, 0], "101": [0, 0], "110": [0, 0], "111": [0, 0]}
        self.correct = 0
        self.total = 0
        self.total_money = 1000

    def get_number(self):
        """Get string from user input. If the input is less than 100 store string and ask for more input."""
        data = input('Print a random string containing 0 or 1:\n\n')
        for x in data:
            if x == '0' or x == '1':
                self.number += x
        if len(self.number) < 100:
            print(f"The current data length is {len(self.number)}, {100 - len(self.number)} symbols left")
            self.get_number()
        else:
            self.generate_profile()

    def generate_profile(self):
        """Iterate the length of the string and search with slices for matches with the keys from the dictionary
         'profile'. If the next number to the last in the triad index is 0 or 1 store in the values of the dict."""
        for y in range(len(self.number) - 3):
            if self.number[y + 3] == "0":
                self.profile[self.number[y:y + 3]][0] += 1
            elif self.number[y + 3] == "1":
                self.profile[self.number[y:y + 3]][1] += 1
        print(f"\nFinal data string:\n{self.number}\n")
        print("You have $1000. Every time the system successfully predicts your next press, you lose $1.")
        print('Otherwise, you earn $1. Print "enough" to leave the game. Let\'s go!\n')

        self.prediction()

    def prediction(self):
        test_string = ""
        number_list = ["0", "1"]

        while test_string != "enough":
            test_string = input("Print a random string containing 0 or 1:\n")
            matched_list = [num in number_list for num in test_string]
            check_matched_list = all(matched_list)
            if test_string == "enough":
                print("Game over!")
                break
            elif check_matched_list == False:
                pass
            else:
                prediction_string = test_string[:3]
                self.total = len(test_string) - 3
                for number in range(self.total):
                    triad = test_string[number:number + 3]
                    prediction_string += '0' if self.profile[triad][0] >= self.profile[triad][1] else '1'
                self.correct = 0
                for x in range(self.total):
                    if prediction_string[x] == test_string[x]:
                        self.correct += 1
                print(f"prediction:\n{prediction_string}\n")
                print("Computer guessed right {} out of {} symbols ({} %)".format(self.correct,
                                                                                  self.total,
                                                                                  (self.correct / self.total) * 100))
                self.money()


    def money(self):
        money_lost = self.correct - (self.total - self.correct)
        self.total_money = self.total_money - money_lost
        print(f"Your capital is now ${self.total_money}\n")



print("Please give AI some data to learn...")
print("The current data length is 0, 100 symbols left")

if __name__ == '__main__':
    GenerateRandomness().get_number()
