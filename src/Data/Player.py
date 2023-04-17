# Player class - represents players in the game. Will contain player score, name (first and last), and codename


class Player:
    def __init__(self, first_name, last_name, code_name):
        self.firstName = first_name
        self.lastName = last_name
        self.codeName = code_name
        self.score = 0
