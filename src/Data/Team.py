# Team class - represents a team in the game. Will contain a list of players on the team, team score,
# and other necessary information
from src.Data import Player


class Team:
    def __init__(self, players: list[Player]):
        self.players = players
        self.score = 0

    # Returns an id for each player
    def hasPlayer(self, id):
        for p in self.players:
            if p.codeName == id:
                return True
        return False

    # Update player score if called
    def playerScored(self, id):
        self.score = self.score + 10
        for p in self.players:
            if p.codeName == id:
                p.score = p.score + 10