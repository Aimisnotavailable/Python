import json

class Brains:

    def __init__(self):
        self.previous_guess = {str(i): 0 for i in range(0,51)}

    def save(self):
        f = open('guess.json', 'w')
        json.dump(self.previous_guess, f)

    def load(self):
        f = open('guess.json', 'r')
        self.previous_guess = json.load(f)

        return self.previous_guess


    def calculate_most_unusual_guess(self):
        pass
