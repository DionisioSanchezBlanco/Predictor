class GenerateRandomness:
    """Generate randomness"""

    def __init__(self):
        """Initiate user input"""
        self.number = ''
        self.profile = {"000": [0, 0], "001": [0, 0], "010": [0, 0], "011": [0, 0],
                        "100": [0, 0], "101": [0, 0], "110": [0, 0], "111": [0, 0]}

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
        self.prediction()

    def prediction(self):
        test_string = input("Please enter a test string containing 0 or 1:\n\n")
        prediction_string = test_string[:3]
        total = len(test_string) - 3
        for number in range(total):
            triad = test_string[number:number + 3]
            prediction_string += '0' if self.profile[triad][0] >= self.profile[triad][1] else '1'
        correct = 0
        for x in range(total):
            if prediction_string[x] == test_string[x]:
                correct += 1
        print(f"prediction:\n{prediction_string}\n")
        print("Computer guessed right {} out of {} symbols ({} %)".format(correct,
                                                                          total,
                                                                          (correct / total) * 100))

print("Please give AI some data to learn...")
print("The current data length is 0, 100 symbols left")

if __name__ == '__main__':
    GenerateRandomness().get_number()
