class Predictor:
    def __init__(self):
        self.string = ''
        self.buffer = ''
        self.test_string = ''
        self.test_buffer = ''
        self.prediction = ''
        self.capital = 1000
        self.correct_predictions = 0
        self.triads = {}
        self.greet()
        self.get_input()
        self.count_triads()
        self.info()
        self.play()

    def greet(self):
        print("Please give AI some data to learn...")
        print("The current data length is 0, 100 symbols left")

    def get_input(self):
        while len(self.string) < 100:
            print("Print a random string containing 0 or 1:\n")
            print()
            self.buffer = input()
            self.filter_string()

    def filter_string(self):
        for char in self.buffer:
            if char in ['0', '1']:
                self.string += char
        if len(self.string) >= 100:
            print("Final data string:")
            print(self.string)
            print()
        else:
            print(f"Current data length is {len(self.string)}, {100 - len(self.string)} symbols left")

    def filter_test_string(self):
        self.test_string = ""
        for char in self.test_buffer:
            if char in ['0', '1']:
                self.test_string += char

    def count_triads(self):
        for i in range(len(self.string)):
            triad = self.string[i:i+3]
            if len(triad) != 3:
                continue
            counts = self.triads.get(triad)

            if counts is None:
                self.triads.update({triad: (1 if triad + "0" == self.string[i:i+4] else 0, 1 if triad + "1" == self.string[i:i+4] else 0)})
            else:
                self.triads.update({triad: (counts[0] + 1 if triad + "0" == self.string[i:i+4] else counts[0], counts[1] + 1 if triad + "1" == self.string[i:i+4] else counts[1])})

    def print_triads(self):
        for triad in sorted(self.triads.items()):
            print(f"{triad[0]}: {triad[1][0]},{triad[1][1]}")

    def get_test_input(self):
        self.test_buffer = input("Print a random string containing 0 or 1:\n")

    def init_three(self):
        keys = []
        values = []
        for key, val in self.triads.items():
            keys.append(key)
            values.append(sum(val))

        self.prediction = keys[values.index(max(values))]

    def get_prediction(self):
        for i in range(0, len(self.test_string) - 3):
            self.prediction += str(self.triads[self.test_string[i:i+3]].index(max(self.triads[self.test_string[i:i+3]])))

        print("prediction: ")
        print(self.prediction)

    def get_accuracy(self):
        self.correct_predictions = 0
        for i, digit in enumerate(self.test_string):
            if i < 3:
                continue
            if digit == self.prediction[i]:
                self.correct_predictions += 1
        accuracy = round(self.correct_predictions / (len(self.test_string) - 3) * 100, ndigits=2)
        print()
        print(f"Computer guessed right {self.correct_predictions} out of {len(self.test_string) - 3} symbols ({accuracy} %)")

    def info(self):
        print(f"You have ${self.capital}. Every time the system successfully predicts your next press, you lose $1.")
        print('Otherwise, you earn $1. Print "enough" to leave the game. Let\'s go!\n')

    def calculate_capital(self):
        self.capital += len(self.test_string) - 3 - 2 * self.correct_predictions
        print(f"Your capital is now ${self.capital}\n")

    def play(self):
        while True:
            self.get_test_input()
            if self.test_buffer == "enough":
                break

            self.filter_test_string()

            if self.test_string == "":
                continue

            self.init_three()
            self.get_prediction()
            self.get_accuracy()
            self.calculate_capital()

        print("Game over!")


predictor = Predictor()
